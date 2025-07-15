

SLOW_FRAMES_COUNT = 3
MED_FRAMES_COUNT = 3
FAST_FRAMES_COUNT = 20

SLOW_FRAME_STEP = 0.3
MED_FRAME_STEP = 0.2
FAST_FRAME_STEP = 0.1


STATE_ZERO = 0
STATE_HALF_SLOW = 0.4
STATE_HALF_MED = 0.5
STATE_HALF_FAST = 0.6
STATE_FULL = 1

SEC_INFINITE = 1000000000

current_sec = 7.0

frames = [
0,
STATE_ZERO,
5,
STATE_ZERO,
7,
STATE_FULL,
]


for i in range(1, SLOW_FRAMES_COUNT+1):
    current_sec += SLOW_FRAME_STEP
    frames += [current_sec, STATE_HALF_SLOW]
    current_sec += SLOW_FRAME_STEP
    frames += [current_sec, STATE_FULL]

for i in range(1, MED_FRAMES_COUNT+1):
    current_sec += MED_FRAME_STEP
    frames += [current_sec, STATE_HALF_MED]
    current_sec += MED_FRAME_STEP
    frames += [current_sec, STATE_FULL]

for i in range(1, FAST_FRAMES_COUNT+1):
    current_sec += FAST_FRAME_STEP
    frames += [current_sec, STATE_HALF_FAST]
    current_sec += FAST_FRAME_STEP
    frames += [current_sec, STATE_FULL]

for i in range(1, MED_FRAMES_COUNT+1):
    current_sec += MED_FRAME_STEP
    frames += [current_sec, STATE_HALF_FAST]
    current_sec += MED_FRAME_STEP
    frames += [current_sec, STATE_FULL]

for i in range(1, SLOW_FRAMES_COUNT+1):
    current_sec += SLOW_FRAME_STEP
    frames += [current_sec, STATE_HALF_FAST]
    current_sec += SLOW_FRAME_STEP
    frames += [current_sec, STATE_FULL]


current_sec += SLOW_FRAME_STEP
frames += [current_sec, STATE_HALF_MED]

current_sec += 1
frames += [SEC_INFINITE, STATE_HALF_MED]


for frame in frames:
    print(f'{frame:.2f}'.replace('.', ','))


print('---')
print(len(frames)/2)
