# bub [ModName] ... String

import os
import sys

def main():
    if len(sys.argv) == 1:
        show_err("must have at least one argument")

    flags = sys.argv[1:-1]

    str_arg = esc_seq(flags) + sys.argv[-1]

    os.system(f"echo -e \"{str_arg}\"")

###################################
############   utils   ############
###################################

def show_err(msg):
  print(f"error: {msg}")
  sys.exit(1)

# converts list of keys to their escape sequence
# eg [bold, black] becomes \e[1;30m
# doesn't handle nums=[], caller must handle
def esc_seq(keys):
    codes = []
    for key in keys:
        if key in mod_map:
            codes.append(str(mod_map[key]))
        else:
            show_err(f"\'{key}\' is an invalid color mod")
    joined = ";".join(codes)
    return f"\\e[{joined}m"

mod_map = {
  'reset': 0,
  'bold': 1,
  'dim': 2,
  'faint': 2,
  'italic': 3,
  'uline': 4,
  'inverse': 7,
  'reverse': 8,
  'sthru': 9,
  'black': 30,
  'red': 31,
  'green': 32,
  'yellow': 33,
  'blue': 34,
  'magenta': 35,
  'cyan':36,
  'white': 37,
  'bblack': 90,
  'bred': 91,
  'bgreen': 92,
  'byellow': 93,
  'bblue': 94,
  'bmagenta': 95,
  'bcyan':96,
  'bwhite': 97,
}

main()
