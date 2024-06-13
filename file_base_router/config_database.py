"""
Configure JSON

"""

from os import mkdir, path, chmod
import json


class Database:
    def __init__(self, database):
        self.config = {
            "database": path.expanduser(database),
            "file": path.join(database, "rconfig.json"),
        }

    def update_config(self):
        mkdir(self.config["database"])
        with open(self.config["file"], "w", encoding="utf-8") as file_path:
            chmod(self.config["file"], 0o774)
            json.dump(self.config, file_path)

    def create_database(self):
        """

        sets default folder for routing files

        """
        dir_exists = path.exists(self.config["database"])
        if not dir_exists:
            print("Setting up database")
            self.update_config()
        else:
            pass
