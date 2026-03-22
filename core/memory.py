import json
from datetime import datetime

MEMORY_FILE = "memory.json"


def save_memory(entry):
    entry["timestamp"] = str(datetime.now())

    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")


def load_memory(limit=5):
    try:
        with open(MEMORY_FILE, "r") as f:
            lines = f.readlines()
            return [json.loads(line) for line in lines[-limit:]]
    except FileNotFoundError:
        return []
