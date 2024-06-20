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
        self._config = {
            "database": path.expanduser(database),
            "file": path.join(database, "rconfig.json"),
            "d_count": 0,
            "f_count": 0,
            "destination": "",
            "destinations": [],
            "criteria": [],
        }

    def create_database(self):
        """

        sets default folder for routing files

        """

        if path.exists(self._config["database"]):
            with open(self._config["file"], "r", encoding="utf-8") as config_f:
                json_data = json.load(config_f)
                self._config["d_count"] = json_data["d_count"]
                self._config["f_count"] = json_data["f_count"]
                self.config["destinations"] = json_data["destinations"]
                self.config["criteria"] = json_data["criteria"]

        else:
            mkdir(self._config["database"])
            with open(self._config["file"], "w", encoding="utf-8") as file_path:
                chmod(self._config["file"], 0o774)
                json.dump(self._config, file_path)

    @property
    def config(self) -> str:
        """config"""
        return self._config

    @config.setter
    def config(self, value: str) -> None:
        self._config = value

    def update_config(self):
        """
        update config file

        """
        with open(self._config["file"], "w", encoding="utf-8") as file_path:
            chmod(self._config["file"], 0o774)
            json.dump(self._config, file_path)
