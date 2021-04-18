#!/usr/bin/env python3

__all__ = []

COLORS = "grey|red|green|yellow|blue|magenta|cyan|white".split("|")
FOREGROUND = list(range(30, 38))
BACKGROUND = list(range(40, 48))

def escape(i):
    return f"\033[{i}m"

RESET = escape(0)

def inject(name, fn):
    globals()[name] = fn
    __all__.append(name)

for i, color in enumerate(COLORS):
    def build(pre, post):
        return lambda string: pre + str(string) + post
    inject(color, build(escape(FOREGROUND[i]), RESET))
    inject("on_" + color, build(escape(BACKGROUND[i]), RESET))
    for j, back in enumerate(COLORS):
        if i != j:
            inject(color + "_on_" + back,
                build(escape(FOREGROUND[i]) + escape(BACKGROUND[j]), RESET)
            )

COLORFNS = list(__all__)
def colored(string: str, color: str) -> str:
    if color in COLORFNS:
        return globals()[color](string)
    else:
        raise ValueError(f"Invalid text color: {color}")
__all__.append("colored")

if __name__ == "__main__":
    print("all colors:")
    code = "\n".join(
        f"print({color}(\"{color.upper()}\"), end=\" \")" for color in COLORS
    )
    exec(code)

    print("\ncolor table:")
    table = "\n".join(
        "".join(
            colored(fore[:4].upper().ljust(4) + back[:4].upper().rjust(4), fore + "_on_" + back) if fore != back
                else " " * 8
        for back in COLORS)
    for fore in COLORS)
    print(table)
