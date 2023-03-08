# bub [ModName] ... String

import os
import sys

esc_char = '\x1b'

def main():
	if len(sys.argv) == 1:
		show_err("must have at least one argument")
	
	mod_code = esc_seq(sys.argv[1:-1])
	print(mod_code + sys.argv[-1], end='')	

def show_err(msg):
  print(f"error: {msg}")
  sys.exit(1)

# converts list of keys to their escape sequence
# eg [bold, black] becomes \e[1;30m
def esc_seq(keys):
    codes = []
    for key in keys:
        if key in mod_map:
            codes.append(str(mod_map[key]))
        else:
            show_err(f"\'{key}\' is an invalid mod code")
    joined = ";".join(codes)
    return f"{esc_char}[{joined}m"

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

for r in [
	range(0,38),
	range(39,48),
	range(49,55),
	range(59,66),
	range(73,76),
	range(90,98),
	range(100,108)]:
	for x in r:
		mod_map.update( {str(x): x} )

main()
