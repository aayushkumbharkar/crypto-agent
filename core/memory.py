import json
from datetime import datetime


def save_memory(data):
    entry = {"timestamp": str(datetime.now()), "data": data}

    with open("memory.json", "a") as f:
        f.write(json.dumps(entry) + "\n")
