"""Recording sheets/plan presentation. This writer must never target DATA."""
import csv
import io
import json
from pathlib import Path


def non_data_path(path):
    path = Path(path).resolve()
    if any(part.lower() == "data" for part in path.parts):
        raise ValueError("Recording preparation cannot write DATA; use DataFolder for future game export")
    return path


def write_recordings(script, output, plan=None):
    output = non_data_path(output)
    files = {"dialogue.design.json": json.dumps(script.data, ensure_ascii=False, indent=2) + "\n"}
    for language in ("ru", "en"):
        sheet = io.StringIO(newline="")
        writer = csv.writer(sheet)
        writer.writerow(["fragment", "role", "pool", "filename", "text"])
        for row in script.fragments:
            writer.writerow([row["id"], row["role"], row["pool"],
                             script.line_name(row) + ".wav", row[language]])
        files[f"{language}/lines.csv"] = sheet.getvalue()
    if plan is not None:
        files["voice_plan.json"] = json.dumps(plan, ensure_ascii=False, indent=2) + "\n"
    # Resolve all paths before writes, including existing links in the destination.
    targets = [(non_data_path(output / relative), content) for relative, content in files.items()]
    if any(not path.is_relative_to(output) for path, _ in targets):
        raise ValueError("Recording file escapes output folder")
    for path, content in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
