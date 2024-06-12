"""
    Instantiate a router object

"""

import os
import json
from config_database import Database


class Router:
    """

    Instantaiate a router object

    """

    def __init__(self, dir_path):

        self.dir = os.path.expanduser(dir_path)
        self.database = Database(self.dir)

    def monitor_dir(self):
        """
        sets default folder for routing files

        """

        dir_exists = os.path.exists(self.dir)
        if not dir_exists:
            print("Setting up database")
            self.database.update_config()
        else:
            pass
