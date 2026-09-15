"""Original procedural sound-design candidates; no field recording or AI generation claimed."""
import math, random, wave, struct, json, hashlib
from pathlib import Path
ROOT = Path(__file__).resolve().parent
SR = 48000
DURATION = 31.233333
N = round(SR * DURATION)
rng = random.Random(110913)
def save(name, function):
    peak = 0.0
    with wave.open(str(ROOT / name), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        for start in range(0, N, 48000):
            values = []
            for i in range(start, min(start+48000, N)):
                v = function(i / SR)
                peak = max(peak, abs(v))
                values.append(round(max(-1,min(1,v))*32767))
            w.writeframes(struct.pack("<"+"h"*len(values), *values))
    return {"file": name, "sample_rate": SR, "channels": 1, "frames": N, "duration_seconds": N/SR, "peak_dbfs": 20*math.log10(max(peak,1e-12)), "sha256": hashlib.sha256((ROOT/name).read_bytes()).hexdigest()}
def edge(t):
    return min(1,t/0.5,max(0,(DURATION-t)/0.5))
state = 0.0
def ambience(t):
    global state
    state = 0.985*state + 0.015*rng.uniform(-1,1)
    return edge(t)*(0.009*math.sin(2*math.pi*50*t)+0.003*math.sin(2*math.pi*100*t)+0.018*state)
# Audible incoming-call motif, not a recording of a particular phone.
# Starts at caller insert; provisional stop at acceptance shot entry.
def phone(t):
    if not 6.067 <= t < 23.167: return 0
    u = (t-6.067)%3.0
    pulse = u if u < 0.32 else u-0.48
    if not (0<=u<0.32 or 0.48<=u<0.80): return 0
    env = min(1,pulse/0.02,max(0,(0.32-pulse)/0.05))
    return 0.055*env*(math.sin(2*math.pi*660*t)+0.4*math.sin(2*math.pi*880*t))
# Original sustained A3/E4 dyad; enters at reach shot, no pre-existing composition.
def cue(t):
    start,end = 16.4,DURATION
    if t<start: return 0
    env=min(1,(t-start)/1.5,max(0,(end-t)/1.0))
    return 0.035*env*(math.sin(2*math.pi*220*t)+0.55*math.sin(2*math.pi*330*t)+0.1*math.sin(2*math.pi*440*t))
files=[save("ambience-kitchen-candidate.wav",ambience),save("sfx-incoming-call-candidate.wav",phone),save("music-reach-cue-candidate.wav",cue)]
(ROOT/"stem-verification.json").write_text(json.dumps({"method":"original procedural synthesis", "files":files,"review_limits":"Technical checks only; no listening, locked sound-bible approval, sync-dialogue or audience review."},indent=2)+"\n")
print(json.dumps(files,indent=2))
