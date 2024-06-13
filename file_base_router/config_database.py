"""
Configure JSON

"""

from os import mkdir, path, chmod
import json


class Database:
    """
    Setup Database

    """

    def __init__(self, database):
        self.config = {
            "database": path.expanduser(database),
            "file": path.join(database, "rconfig.json"),
            "d_count": 0,
            "f_count": 0,
        }

        if path.exists(self.config["database"]):
            with open(self.config["file"], "r", encoding="utf-8") as config_f:
                json_data = json.load(config_f)
                self.config["d_count"] = json_data["d_count"]
                self.config["f_count"] = json_data["f_count"]

        else:
            mkdir(self.config["database"])
            with open(self.config["file"], "w", encoding="utf-8") as file_path:
                chmod(self.config["file"], 0o774)
                json.dump(self.config, file_path)

    def update_config(self):
        """
        update config file

        """
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
