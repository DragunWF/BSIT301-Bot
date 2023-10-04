import json
from pathlib import Path


class Data:
    cwd = Path.cwd()
    settings = json.loads(
        Path(f"{Path.cwd()}/config/settings.json").read_text()
    )
