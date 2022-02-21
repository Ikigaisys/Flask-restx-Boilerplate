import json
from pathlib import Path


class Settings:
    settings = None

    def __getattr__(cls, key):
        if key in cls.settings:
            return cls.settings[key]


settings = None
if not settings:
    settings = Settings()
    project_root = str(Path(__file__).parent.parent.parent)
    with open(f"{project_root}/etc/settings.json", "r") as file:
        configs = json.load(file)
        settings.settings = configs
