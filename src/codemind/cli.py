#!/usr/bin/env python3
"""codemind CLI"""

import argparse
import sys
from codemind.core import Core, create_core, Config


def main() -> int:
    parser = argparse.ArgumentParser(prog="codemind")
    parser.add_argument("command", choices=["run", "help"])
    parser.add_argument("input", nargs="?", default="default")
    
    args = parser.parse_args()
    
    if args.command == "help":
        parser.print_help()
        return 0
    
    core = create_core(Config(name="codemind"))
    result = core.execute(args.input)
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
