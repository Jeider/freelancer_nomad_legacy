import unittest

from story.cutscenes.old_format import ThnParseError, parse_old_motions


class OldFormatTests(unittest.TestCase):
    def motion(self, delay='0', targets='"Char_trent"', props='animation="walk", duration=2'):
        return '{' + delay + ', START_MOTION, {' + targets + '}, {' + props + '}}'

    def test_legacy_keys_and_targets(self):
        event, = parse_old_motions(self.motion())
        self.assertEqual(event['delay'], 0)
        self.assertEqual(event['animation'], 'walk')
        self.assertFalse(event['facial'])
        self.assertEqual(event['targets'], ['Char_trent'])
        self.assertEqual(event['parameters']['duration'], '2')

    def test_comments_do_not_create_events(self):
        motion = self.motion()
        text = '-- ' + motion + '\n--[=[' + motion + ']=]\nnote=[[' + motion + ']]\nevents={' + motion + '}'
        self.assertEqual(len(parse_old_motions(text)), 1)

    def test_comments_inside_fields(self):
        text = '{0,-- time\n START_MOTION, {"trent"}, {animation=-- name\n"walk"}}'
        event, = parse_old_motions(text)
        self.assertEqual(event['animation'], 'walk')
        self.assertIn('-- name\n', event['props'])

    def test_nested_properties_and_string_contents_preserved(self):
        props = 'animation="walk", extra={a={1,2}, s="} --  two  spaces"}, flags=A+B'
        event, = parse_old_motions(self.motion(props=props))
        self.assertEqual(event['props'], '{' + props + '}')
        self.assertEqual(event['parameters']['extra'], '{a={1,2}, s="} --  two  spaces"}')
        self.assertEqual(event['parameters']['flags'], 'A+B')

    def test_signed_exponents_and_source_order(self):
        events = parse_old_motions('events={' + self.motion('+2e1') + ',' + self.motion('-.5E-1') + '}')
        self.assertEqual([e['delay'] for e in events], [20, -.05])

    def test_quotes_escapes_and_multiple_targets(self):
        event, = parse_old_motions(self.motion(targets="'Char_trent', [=[second]=]",
                                             props=r"animation='it\'s\032fine'"))
        self.assertEqual(event['animation'], "it's fine")
        self.assertEqual(event['targets'], ['Char_trent', 'second'])

    def test_semicolons_and_trailing_separators(self):
        event, = parse_old_motions('{0; START_MOTION; {"trent";}; {animation="walk";};}')
        self.assertEqual(event['animation'], 'walk')

    def test_facial_classification(self):
        events = parse_old_motions(self.motion(props='animation="Sc_dx_s038x_4202_kress"') +
                                  self.motion(props='animation="Sc_MLBODY_STND_IDLE_000LV_XB_04"'))
        self.assertEqual([e['facial'] for e in events], [True, False])

    def test_other_events_are_not_motions(self):
        self.assertEqual(parse_old_motions('{0, START_SOUND, {"sound"}, {}}'), [])

    def test_repeated_properties_preserved(self):
        event, = parse_old_motions(self.motion(props='animation="a", trans_time=2, trans_time=1'))
        self.assertEqual(event['parameters']['trans_time'], '1')
        self.assertEqual(event['props'].count('trans_time'), 2)

    def test_malformed_motions_are_errors(self):
        cases = [self.motion(delay='1e999'), self.motion(delay='t+1'),
                 self.motion(targets=''), self.motion(targets='actor'),
                 self.motion(props='duration=2'), self.motion(props='animation=clip'),
                 self.motion(props='animation=""'),
                 '{0, START_MOTION, {"trent"}}', '{0, START_MOTION, {}, {}, 5}',
                 self.motion()[:-1], self.motion(props='animation="unterminated'),
                 self.motion(props='animation="a",, duration=1'), '--[[unfinished',
                 '{0 START_MOTION, {"trent"}, {animation="walk"}}']
        for text in cases:
            with self.subTest(text=text), self.assertRaisesRegex(ThnParseError, r'line \d+, column \d+'):
                parse_old_motions(text)

    def test_error_location(self):
        with self.assertRaisesRegex(ThnParseError, r'line 2, column 2'):
            parse_old_motions('\n{bad, START_MOTION, {"trent"}, {animation="walk"}}')


if __name__ == '__main__':
    unittest.main()
