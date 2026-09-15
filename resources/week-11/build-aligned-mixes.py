"""Render PCM mixes on Cut A's 48 kHz timeline; originals are excluded."""
import wave, array, math, json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SR=48000; N=1499200
VOICE_START=27.8; CALL_START=6.067; CALL_END=24.1; CUE_START=17.6

def read(name):
    with wave.open(str(ROOT/name)) as w:
        assert w.getnchannels()==1 and w.getframerate()==SR and w.getsampwidth()==2
        return array.array('h',w.readframes(w.getnframes()))

def write(name, values):
    vals=array.array('h',(round(v) for v in values))
    assert len(vals)==N and max(abs(x) for x in vals)<32767
    with wave.open(str(ROOT/name),'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(vals.tobytes())
    peak=max(abs(x) for x in vals)
    return {'file':name,'duration_seconds':N/SR,'peak_dbfs':20*math.log10(max(1,peak)/32768),'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()}

amb=read('ambience-kitchen-candidate.wav')
sfx=[]; music=[]
for i in range(N):
    t=i/SR; v=0
    if CALL_START<=t<CALL_END:
        u=(t-CALL_START)%3
        pulse=u if u<0.32 else u-0.48
        if 0<=u<0.32 or 0.48<=u<0.8:
            env=min(1,pulse/0.02,max(0,(0.32-pulse)/0.05),max(0,(CALL_END-t)/0.03))
            v=0.055*env*(math.sin(2*math.pi*660*t)+0.4*math.sin(2*math.pi*880*t))
    sfx.append(v*32767)
    env=0 if t<CUE_START else min(1,(t-CUE_START)/1.5,max(0,(N/SR-t)/1))
    music.append(0.035*env*(math.sin(2*math.pi*220*t)+0.55*math.sin(2*math.pi*330*t)+0.1*math.sin(2*math.pi*440*t))*32767)
records=[write('sfx-incoming-call-aligned.wav',sfx),write('music-reach-cue-aligned.wav',music)]
for take in ['a','b']:
    raw=read('voice-take-'+take+'.wav')
    assert len(raw)>1000
    # Same fixed peak gain in both renders, no time stretching.
    gain=0.32*32767/max(max(abs(x) for x in read('voice-take-a.wav')),max(abs(x) for x in read('voice-take-b.wav')))
    dialog=[0.0]*N
    offset=round(VOICE_START*SR)
    for j,x in enumerate(raw):
        if offset+j<N: dialog[offset+j]=x*gain
    records.append(write('dialogue-only-'+take+'.wav',dialog))
    records.append(write('full-pass-'+take+'.wav',[dialog[i]+amb[i]+sfx[i]+music[i] for i in range(N)]))
    if take=='a': records.append(write('no-music-control.wav',[dialog[i]+amb[i]+sfx[i] for i in range(N)]))
(ROOT/'alignment-verification.json').write_text(json.dumps({'working_picture':'Week 10 Cut A; provisional choice','voice_engine':'macOS Samantha; rate A=150, B=105 wpm; actual independent synthesis','voice_start_seconds':VOICE_START,'call_start_seconds':CALL_START,'call_stop_seconds':CALL_END,'music_start_seconds':CUE_START,'voice_selection':'A provisionally used for primary pair; technical timing choice, no listening-based performance selection claimed','alignment_method':'Ending contact sheet at 4fps and 27.3–28.9s samples at 10fps; event-aligned ADR, no phoneme-exact lip-sync claim','original_audio':'Excluded from both versions to avoid duplicate/unverified dialogue and music','files':records,'review_limits':'No auditory or independent audience review. Mouth remains open over multiple frames; event alignment does not establish exact phoneme match.'},indent=2)+'\n')
print('Aligned mixes rendered and peak-checked.')
