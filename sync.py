import srt
from datetime import timedelta

INPUT = "You've Got Mail (si).srt"
OUTPUT = "out.srt"
START = 1411
END = -1
SHIFT = timedelta(milliseconds=1000)

with open(INPUT) as f:
    subs = list(srt.parse(f.read()))

for sub in subs[START-1:END]:
    sub.start += SHIFT
    sub.end += SHIFT

with open(OUTPUT, 'w') as f:
    f.write(srt.compose(subs))
