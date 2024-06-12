"""
Configure JSON

"""

from os.path import join
from os import mkdir
import json


class Database:
    def __init__(self, database):
        self.config = {
            "database": database,
            "file": join(database, "rconfig.json"),
        }

    def update_config(self):
        mkdir(self.config["database"])
        with open(self.config["file"], "w", encoding="utf-8") as path:
            json.dump(self.config, path)
