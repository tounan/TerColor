# TerColor

Yet another termcolor module

Colors: grey red green yellow blue magenta cyan white

Functions:

- color names, like `red()`
- background colors, like `on_red()`
- combination of the two, `white_on_red()`
- the `colored(string, colors)`, e.g. `colored("foo", "white_on_red")`, but NOT `colored("foo", "white", "on_red")`

Note that there is no `cprint()`, and `red_on_red` is not allowed
