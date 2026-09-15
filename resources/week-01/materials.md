# Week 1 real production material — The Unanswered Call

This is a standalone AI-directing demonstration for Week 1. It is not the learner's eventual film and it is deliberately not a production asset for the placeholder story “Table for One.”

## Teaching purpose

The pair demonstrates the complete Week 1 loop:

**direct → generate → evaluate → redirect**

The objective and intended audience interpretation remain fixed. Only the playable action, timing, emphasis, and degree change between the two takes.

## Locked material

- **Scene:** A woman sits alone at a kitchen table at night. A phone beside her vibrates once.
- **Character:** A woman in her late twenties, short dark bob, oatmeal-coloured sweater.
- **Setting and frame:** Modest kitchen, warm overhead light, dark window, static medium close-up at seated eye level.
- **Objective:** She wants to answer the call but consciously prevents herself from doing so.
- **Intended interpretation:** The audience reads restraint as a difficult choice, not indifference, boredom, or an absent-minded pause.
- **Continuity rule:** Character, costume, set, phone, lighting, composition, and camera remain as consistent as the model allows.

## Note A → Take A

**Note A:** When the phone vibrates, look toward it, begin reaching with the right hand, stop before touching it, and slowly withdraw.

- Full generation prompt: [prompt-a.txt](./prompt-a.txt)
- Generated take: [take-a.mp4](./take-a.mp4)

**Diagnosis:** The take establishes the scene and produces a reach-and-withdraw action, but the stop is too soft and the performance remains generally downcast. Without being told the objective, the behaviour can read as ordinary hesitation, sadness, or distraction. The moment of actively preventing herself from answering is not unmistakable. The hand also comes very close to the phone, weakening the requested “stop before touching” boundary.

## Note B → Take B

**Note B:** At the vibration, inhale and snap the eyes to the phone; reach urgently; stop the fingertips two centimetres above it and hold for a full second with tense fingers and a tightened jaw; then deliberately withdraw the hand into the lap while keeping the eyes fixed on the phone, ending on a controlled exhale.

- Full redirect/remix prompt: [prompt-b.txt](./prompt-b.txt)
- Generated take: [take-b.mp4](./take-b.mp4)

**Why this is a genuine redirect:** Note B does not change what the character wants or what the audience should understand. It targets the diagnosed gap by changing only observable behaviour: onset speed, stopping distance, duration of the hover, muscular tension, eye line, and the endpoint of the withdrawal.

**What changed and why:** Take B turns an ambiguous slow reach into a legible act of self-restraint by adding an urgent eye-and-hand response, a sustained unfinished reach, and a deliberate withdrawal while preserving the original objective.

## Suggested lecture use

1. Show Take A without revealing the note and ask what the character appears to want.
2. Reveal the fixed objective, intended interpretation, and Note A; identify the gap between intention and result.
3. Reveal Note B one clause at a time and ask which diagnosed failure each clause targets.
4. Show Take B without announcing that it is the “better” take; collect observable differences before discussing interpretation.
5. Compare the two readings and stress that specificity is useful only when it serves a fixed objective.

Do not use this lecture segment to explain the workshop. The workshop should begin with its own short recap of the lecture's chain.

## QA record

- Generated with `sora-2` on 2026-09-11 through the OpenAI Videos API.
- Take A video job: `video_6aa37b050670819196c96f69f096524f07c717edb128fca7`.
- Take B remix job: `video_6aa37ccfbe40819383a9da4a911d4b8302d93698f58faa2f`.
- Both files: 8.0 seconds, 1280×720, 30 fps, H.264 video, AAC stereo audio.
- Visual inspection: one character; stable identity, wardrobe, setting, phone, lighting, and static camera; no visible text or subtitles. Take B is framed slightly closer than Take A, a minor continuity difference worth naming in class.
- Speech-transcription check: empty transcript for both takes; no recognizable dialogue detected.
- Audio is present and non-silent in both files. The instructor should still listen once before publication to confirm the intended room tone, vibration, and breath cues and the absence of unwanted music.
- Take A SHA-256: `d6c24a60b1075162cdd39e484b88c3123b146f9b6afe689e647d10b54a9e877f`.
- Take B SHA-256: `7b016aa321a68ddf41b1f25f71644ac484df4550ef61018491a5070f953b78e3`.

## Integration boundary

The existing Week 1 lecture and deck still describe a “Table for One” placeholder demonstration. They were intentionally left unchanged. When CC integrates this pack, the placeholder section should be replaced with this standalone demonstration and the surrounding wording should stop claiming that the real pair was generated from the “Table for One” scene. The generated files themselves are ready; website/deck integration remains a separate change requiring the owner's approval.
