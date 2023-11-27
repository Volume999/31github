import sys
import json

def main():
    result = {"items": [
        {
            "uid": "desktop",
            "type": "file",
            "title": "Desktop",
            "subtitle": "~/Desktop",
            "arg": "Hello!",
            "autocomplete": "Desktop",
        }
    ]}  

    sys.stdout.write(json.dumps(result))

if __name__ == "__main__":
    main()