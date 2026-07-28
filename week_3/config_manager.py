from pathlib import Path
import json

open_file  = "settings.json"
with open (open_file, "r") as f:
    data = json.load(f)

print(data)
