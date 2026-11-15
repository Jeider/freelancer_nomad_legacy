"""Read motion tables from text THN without executing Lua.

This is a structural extractor, not a Lua interpreter or a scene converter.
Other event types are left to their respective importers. Expressions in motion
properties are preserved verbatim; delay and animation must be literals.
"""
import math
import re
from dataclasses import dataclass


class ThnParseError(ValueError):
    """Malformed source, with a one-based line and column."""


@dataclass(frozen=True)
class Token:
    kind: str
    value: str
    start: int
    end: int


_NUMBER = re.compile(r'(?:\d+\.\d*|\.\d+|\d+)(?:[eE][+-]?\d+)?')
_NAME = re.compile(r'[A-Za-z_][A-Za-z_0-9]*')
_LONG = re.compile(r'\[(=*)\[')


def _error(text, offset, message):
    line = text.count('\n', 0, offset) + 1
    column = offset - text.rfind('\n', 0, offset)
    raise ThnParseError(f'{message} at line {line}, column {column}')


def _tokens(text):
    i = 0
    while i < len(text):
        if text[i].isspace() or (i == 0 and text[i] == '\ufeff'):
            i += 1
            continue
        start = i
        comment = text.startswith('--', i)
        if comment:
            i += 2
        long = _LONG.match(text, i)
        if long:
            closing = ']' + long[1] + ']'
            end = text.find(closing, long.end())
            if end < 0:
                _error(text, start, 'Unterminated long comment' if comment else 'Unterminated long string')
            value = text[long.end():end]
            if value.startswith('\r\n'):
                value = value[2:]
            elif value.startswith('\n'):
                value = value[1:]
            i = end + len(closing)
            if not comment:
                yield Token('string', value, start, i)
            continue
        if comment:
            end = text.find('\n', i)
            i = len(text) if end < 0 else end
            continue
        if text[i] in '\"\'':
            quote = text[i]
            i += 1
            value = []
            while i < len(text) and text[i] != quote:
                char = text[i]
                if char in '\r\n':
                    _error(text, i, 'Unescaped newline in string')
                if char == '\\':
                    i += 1
                    if i == len(text):
                        _error(text, start, 'Unterminated string')
                    char = text[i]
                    if char.isdigit() and char.isascii():
                        digits = re.match(r'\d{1,3}', text[i:])[0]
                        if int(digits) > 255:
                            _error(text, i, 'Decimal string escape exceeds 255')
                        value.append(chr(int(digits)))
                        i += len(digits)
                        continue
                    char = {'a': '\a', 'b': '\b', 'f': '\f', 'n': '\n',
                            'r': '\r', 't': '\t', 'v': '\v'}.get(char, char)
                    if char == '\r' and text[i:i + 2] == '\r\n':
                        i += 1
                        char = '\n'
                value.append(char)
                i += 1
            if i == len(text):
                _error(text, start, 'Unterminated string')
            i += 1
            yield Token('string', ''.join(value), start, i)
            continue
        match = _NUMBER.match(text, i) or _NAME.match(text, i)
        if match:
            i = match.end()
            kind = 'number' if _NUMBER.fullmatch(match[0]) else 'name'
            yield Token(kind, match[0], start, i)
        else:
            i += 1
            yield Token('symbol', text[start:i], start, i)


class MotionReader:
    def __init__(self, text):
        self.text = text
        self.tokens = list(_tokens(text))
        self.pairs = {}
        stack = []
        for i, token in enumerate(self.tokens):
            if token.kind != 'symbol':
                continue
            if token.value in ('{', '[', '('):
                stack.append(i)
            elif token.value in ('}', ']', ')'):
                if not stack or self.tokens[stack[-1]].value != {'}': '{', ']': '[', ')': '('}[token.value]:
                    _error(text, token.start, 'Unmatched closing delimiter')
                opening = stack.pop()
                self.pairs[opening] = i
        if stack:
            _error(text, self.tokens[stack[-1]].start, 'Unclosed delimiter')

    def fail(self, index, message):
        _error(self.text, self.tokens[index].start, message)

    def fields(self, opening):
        end = self.pairs[opening]
        result = []
        start = i = opening + 1
        while i < end:
            token = self.tokens[i]
            if i in self.pairs:
                i = self.pairs[i] + 1
                continue
            if token.kind == 'symbol' and token.value in (',', ';'):
                if start == i:
                    self.fail(i, 'Empty table field')
                result.append((start, i))
                start = i + 1
            i += 1
        if start < end:
            result.append((start, end))
        return result

    def table(self, span, label):
        start, end = span
        if self.tokens[start].value != '{' or self.pairs.get(start) != end - 1:
            self.fail(start, f'{label} must be a literal table')
        return self.fields(start)

    def string(self, span, label):
        start, end = span
        if end != start + 1 or self.tokens[start].kind != 'string':
            self.fail(start, f'{label} must be a literal string')
        return self.tokens[start].value

    def motions(self):
        result = []
        consumed = set()
        for opening in sorted(self.pairs):
            if self.tokens[opening].value != '{':
                continue
            fields = self.fields(opening)
            motion_fields = [n for n, (a, b) in enumerate(fields)
                             if b == a + 1 and self.tokens[a].kind == 'name'
                             and self.tokens[a].value == 'START_MOTION']
            if not motion_fields:
                continue
            if motion_fields != [1] or len(fields) != 4:
                self.fail(opening, 'START_MOTION requires delay, type, targets and properties')
            consumed.add(fields[1][0])
            a, b = fields[0]
            number = self.tokens[a:b]
            if (len(number) == 2 and number[0].value in ('+', '-')
                    and number[0].kind == 'symbol'):
                number = number[1:]
            if len(number) != 1 or number[0].kind != 'number':
                self.fail(a, 'Motion delay must be a literal number')
            delay = float(''.join(t.value for t in self.tokens[a:b]))
            if not math.isfinite(delay):
                self.fail(a, 'Motion delay must be finite')
            targets = [self.string(span, 'Motion target')
                       for span in self.table(fields[2], 'Motion targets')]
            if not targets or any(not target for target in targets):
                self.fail(fields[2][0], 'Motion requires nonempty targets')
            parameters = {}
            animation = None
            for a, b in self.table(fields[3], 'Motion properties'):
                if b - a < 3 or self.tokens[a].kind != 'name' or self.tokens[a + 1].value != '=':
                    self.fail(a, 'Motion property must have the form name=value')
                key = self.tokens[a].value
                # Preserve all occurrences in props; expose the last textual
                # value in the convenience mapping for repeated named keys.
                parameters[key] = self.text[self.tokens[a + 2].start:self.tokens[b - 1].end]
                if key == 'animation':
                    animation = self.string((a + 2, b), 'Motion animation')
            if not animation:
                self.fail(fields[3][0], 'Motion requires a nonempty animation')
            a, b = fields[3]
            result.append({
                'delay': delay, 'animation': animation, 'targets': targets,
                'props': self.text[self.tokens[a].start:self.tokens[b - 1].end],
                'parameters': parameters,
            })
        for i, token in enumerate(self.tokens):
            if token.kind == 'name' and token.value == 'START_MOTION' and i not in consumed:
                self.fail(i, 'START_MOTION is not in a supported literal event table')
        return result


def parse_motion_tables(text):
    """Return motions in source order; properties retain original Lua spelling."""
    return MotionReader(text).motions()
