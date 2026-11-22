"""Compile RU dispatchers to loose WAVs. No TTS, scene build or engine changes.

The caller supplies freshly generated INIs, or uses the installed ones. All
records are prepared before DataFolder publishes anything or removes a UTF.
"""
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess

VOICES = ('dispatcher01', 'dispatcher02', 'dispatcher03')
INIS = ('AUDIO/voices_space_male.ini', 'AUDIO/voices_space_female.ini')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def utf_leaves(raw):
    """Read every audio leaf, including repeated native IDs, without conversion."""
    h=struct.unpack_from('<14I',raw)
    if h[0]!=0x20465455 or h[1]!=0x101 or h[5]!=44:
        raise ValueError('Expected legacy audio UTF')
    result=[];visited=set()
    def visit(offset):
        while True:
            if offset in visited:raise ValueError('UTF node cycle')
            visited.add(offset)
            if offset+44>h[3]:raise ValueError('UTF node out of bounds')
            sibling,name,flags,_,child,_,_,size=struct.unpack_from('<8I',raw,h[2]+offset)
            start=h[6]+name
            label=raw[start:raw.index(0,start)].decode('ascii')
            if flags&16:
                if child:visit(child)
            else:
                content=raw[h[9]+child:h[9]+child+size]
                if len(content)!=size:raise ValueError('Truncated UTF leaf')
                result.append((label.lower(),content))
            if not sibling:break
            offset=sibling
    visit(0)
    return result


@lru_cache(maxsize=None)
def audio_key(game, code):
    run=subprocess.run([str(Path(game)/'createid.exe'),'-h','-oc',code],
                       cwd=game,capture_output=True,text=True)
    # Retail utility prints a valid ID with exit status 1.
    return '0x'+format(int(run.stdout.split(',')[1].strip(),16),'x')


def duration(raw):
    if raw[:4]!=b'RIFF' or raw[8:12]!=b'WAVE' or struct.unpack_from('<I',raw,4)[0]+8!=len(raw):
        raise ValueError('Expected complete RIFF WAVE')
    chunks={};offset=12
    while offset+8<=len(raw):
        name,size=struct.unpack_from('<4sI',raw,offset)
        if offset+8+size>len(raw):raise ValueError('Truncated WAV chunk')
        chunks[name]=raw[offset+8:offset+8+size];offset+=8+size+(size&1)
    kind,channels,rate,_,align,bits=struct.unpack_from('<HHIIHH',chunks[b'fmt '])
    if not channels or not rate or not chunks.get(b'data'):raise ValueError('Empty WAV')
    if kind==1:
        if not align or len(chunks[b'data'])%align:raise ValueError('Incomplete PCM frame')
        frames=len(chunks[b'data'])//align
    elif kind==0x55:
        frames=struct.unpack_from('<I',chunks[b'fact'])[0]
    else:raise ValueError('Unsupported WAV codec')
    if frames<=0:raise ValueError('No audio frames')
    return frames/rate


def read_audio(path):
    raw=path.read_bytes()
    if raw[:4]==b'RIFF':duration(raw);return raw
    # Existing manually cut MP3 sources are decoded, with no trimming/filtering.
    run=subprocess.run(['ffmpeg','-v','error','-i',str(path),'-ac','1','-ar','24000',
                        '-c:a','pcm_s16le','-f','wav','pipe:1'],capture_output=True)
    if run.returncode:raise ValueError(f'Cannot decode {path}: '+run.stderr.decode(errors='replace'))
    raw=bytearray(run.stdout)
    # ffmpeg's pipe has streaming sizes; close its PCM RIFF before publishing.
    struct.pack_into('<I',raw,4,len(raw)-8)
    offset=12
    while offset+8<=len(raw):
        name,size=struct.unpack_from('<4sI',raw,offset)
        if name==b'data' and size==0xffffffff:
            struct.pack_into('<I',raw,offset+4,len(raw)-offset-8);break
        offset+=8+size+(size&1)
    raw=bytes(raw);duration(raw);return raw


def value(block,key):
    match=re.search(r'(?mi)^\s*'+key+r'\s*=\s*([^;\r\n]+)',block)
    return match[1].strip() if match else ''


def plan(project, folder, ini_files=None):
    project=Path(project).resolve();game=folder.get_root()
    files=dict(ini_files or {name:folder.data_path(name).read_bytes() for name in INIS})
    banks={};metadata={};sources={};records={};missing={};used_hashes={}
    for voice in VOICES:
        bank=folder.data_path(f'AUDIO/{voice}.utf')
        leaves=utf_leaves(bank.read_bytes()) if bank.exists() else []
        banks[voice]=leaves
        metadata[voice]={'source_utf_sha256':digest(bank.read_bytes()) if bank.exists() else None,
                         'archive_leaves':[], 'recordings':{}}
        source_root=project.parent/'PILOTS'/voice
        candidates={}
        for path in sorted(source_root.rglob('*')):
            if path.suffix.lower() in ('.wav','.mp3') and 'RAW' not in path.relative_to(source_root).parts:
                candidates.setdefault(path.stem.lower(),[]).append(path)
        sources[voice]=candidates;records[voice]={};missing[voice]=[];used_hashes[voice]={}
    for ini in INIS:
        raw=files[ini]
        text=raw.decode('utf-8-sig') if isinstance(raw,bytes) else raw
        blocks=re.split(r'(?m)(?=^\[)',text)
        active=''
        for i,block in enumerate(blocks):
            if re.match(r'(?i)^\[voice\]',block):
                active=(value(block,'nickname') or value(block,'extend')).lower()
            if active not in VOICES or not re.match(r'(?i)^\[(sound|voicesound)\]',block):continue
            code=value(block,'msg');key=code.lower()
            if not re.fullmatch(r'[a-zA-Z0-9_+\-]+',code):raise ValueError('Unexpected sound ID: '+code)
            if key not in records[active]:
                # WAV authoring takes have precedence; use existing MP3 authoring
                # files next. The archive is a complete lossless fallback.
                choices=sources[active].get(key,[])
                choices.sort(key=lambda p:(p.suffix.lower()!='.wav',str(p)))
                source=choices[0] if choices else None
                leaf=next((blob for name,blob in banks[active] if name==audio_key(str(game),code)),None)
                live=folder.data_path(f'AUDIO/MOD/{active}/{code}.wav')
                if source:
                    content=read_audio(source);origin=str(source)
                elif leaf is not None:
                    content=leaf;origin='utf:'+audio_key(str(game),code)
                elif live.exists():
                    content=live.read_bytes();origin=str(live)
                else:
                    records[active][key]=None;missing[active].append(code);continue
                seconds=duration(content)
                target=f'AUDIO/MOD/{active}/{code}.wav'
                files[target]=content
                records[active][key]=(target,seconds)
                used_hashes[active][digest(content)]=target
                metadata[active]['recordings'][code]={'file':target,'sha256':digest(content),'duration':seconds,'source':origin}
            record=records[active][key]
            if record is None:continue  # Pre-existing unrecorded IDs remain explicitly reported.
            target,seconds=record
            block=re.sub(r'(?mi)^\s*(?:file|duration)\s*=[^\n]*\n?', '',block)
            # The client parses file immediately, so msg must precede file.
            block=re.sub(r'(?mi)^(\s*msg\s*=[^\n]*\n)',
                         lambda m:m[1]+f'duration = {seconds:.6f}\nfile = '+target.replace('/','\\')+'\n',block, count=1)
            blocks[i]=block
        files[ini]=''.join(blocks).encode('utf-8')
    report={'voices':{}}
    for voice in VOICES:
        # Retain every original waveform, including unmapped IDs and overridden
        # takes, as individual editable WAVs. No duplicate full archive backup.
        for name,content in banks[voice]:
            duration(content)
            fingerprint=digest(content)
            target=used_hashes[voice].get(fingerprint)
            if not target:
                target=f'AUDIO/MOD/{voice}/archive/{name}_{fingerprint[:12]}.wav'
                files[target]=content;used_hashes[voice][fingerprint]=target
            metadata[voice]['archive_leaves'].append({'id':name,'file':target,'sha256':fingerprint})
        old_manifest=folder.data_path(f'AUDIO/MOD/{voice}/manifest.json')
        if not banks[voice] and old_manifest.exists():
            old=json.loads(old_manifest.read_text(encoding='utf-8'))
            metadata[voice]['archive_leaves']=old.get('archive_leaves',[])
            metadata[voice]['source_utf_sha256']=old.get('source_utf_sha256')
        # Historical archive metadata is optional provenance, not a build input.
        required_missing=[code for code in missing[voice] if code.startswith(('tc_','te_'))]
        if required_missing:raise ValueError('Missing courier recordings: '+', '.join(required_missing))
        metadata[voice]['unrecorded_ids']=missing[voice]
        files[f'AUDIO/MOD/{voice}/manifest.json']=(json.dumps(metadata[voice],ensure_ascii=False,indent=2)+'\n').encode('utf-8')
        report['voices'][voice]={'recordings':len(metadata[voice]['recordings']),
                                'archive_leaves_preserved':len(metadata[voice]['archive_leaves']),
                                'unrecorded_ids':missing[voice]}
    return files,report


def compile_dispatchers(project, folder, ini_files=None, *, dry_run=False, output=None):
    files,report=plan(project,folder,ini_files)
    if not dry_run:folder.sync_ru_dispatcher_files(files,VOICES)
    report['dry_run']=dry_run
    if output:
        output=Path(output);output.mkdir(parents=True,exist_ok=True)
        (output/'dispatcher_files.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report


def main(argv=None):
    import argparse
    from tools.data_folder import DataFolder
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(argv)
    project=Path(__file__).resolve().parents[1]
    report=compile_dispatchers(project,DataFolder(root=project.parent.parent),dry_run=args.dry_run,
                               output=args.output or project/'results/dispatcher_files')
    for voice,row in report['voices'].items():
        print(voice, row['recordings'],'WAVs;',len(row['unrecorded_ids']),'pre-existing unrecorded IDs')
    print('Prepared only; no DATA changes' if args.dry_run else 'WAV/INI verified; dispatcher UTFs removed')
