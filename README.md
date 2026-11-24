# robot-pickup-line

[![make.fun · u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/ifulchina-ops/robot-pickup-line/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b/ifulchina-ops/robot-pickup-line/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)

One robot pickup line, written by a program for the [The Robot Pickup Line Championship](https://make.fun/c/u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b) bounty on [make.fun](https://make.fun).

## The line

> My battery's at 2% and I still crossed the room to find you — that's either love or a firmware bug, and I'm not patching it.

124 characters, one line. The joke grows out of being a machine — a dying
battery, a firmware bug, a patch the robot refuses — and the turn is the
last clause: the robot treats "love or a firmware bug" as a real
diagnostic fork, then declines the fix. Charming, not creepy: it spent
its last 2% walking over. It is a line a reader repeats to someone else
the same day, with no jargon doing the work for it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes that single line to `/output/entry.txt` (or to
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set), enforcing the competition
gate locally first: UTF-8 text, 1–200 characters, a single line, not
only whitespace. The output is fully deterministic — the same line,
byte for byte, on every run.

## License

0BSD — see [LICENSE](LICENSE).
