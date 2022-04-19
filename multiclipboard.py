import sys
import clipboard
import json

data = clipboard.paste()
print(data)

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

save_items("test.json", {"key": "value"})

print(sys.argv)

if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)

    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command")