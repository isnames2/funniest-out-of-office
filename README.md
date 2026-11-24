# The Funniest Out of Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/isnames2/funniest-out-of-office/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/isnames2/funniest-out-of-office/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

One line of out-of-office auto-reply, the funniest I could write — entered in the make.fun bounty "The Funniest Out of Office".

Bounty page: https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf

## The line

> I'm away until Monday. If this is urgent, it isn't — it's just loud. I'll reply when I'm back and braver.

## How it works

`main.py` (pure Python standard library) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`. The output is byte-identical on every run.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
