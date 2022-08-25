#!/usr/bin/python3
if __name == "__main__":
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.arg[0]:
            result += int(arg)
            print(result)
