import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

data = clipboard.paste()
print(data)

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_items(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data

save_items("test.json", {"key": "value"})

print(sys.argv)

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == "save":
        print("save")
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command")