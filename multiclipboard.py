import sys
import clipboard
import json

data = clipboard.paste()
print(data)

print(sys.argv)

if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)