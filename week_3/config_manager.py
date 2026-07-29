from pathlib import Path
import json 


with open (Path("settings.json"), "r") as f:
    data = json.load(f)


data["debug_mode"] = True
data["environment"] = "staging"


output_path = Path("updated_settings.json")
with open(output_path, "w") as f:
    json.dump(data, f, indent=4)

print("Successfully generated updated_settings.json!")
