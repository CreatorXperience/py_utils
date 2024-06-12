"""
    Instantiate a router object

"""

import os


class Router:
    """
    Instantaiate a router object

    """

    def __init__(self, dir_path):

        self.dir = os.path.expanduser(dir_path)

    def monitor_dir(self):
        """
        sets default folder for routing files

        """

        dir_exists = os.path.exists(self.dir)
        if not dir_exists:
            print("Setting up database")
            os.mkdir(self.dir)
            default_file_path = "rconfig.json"
            with open(
                os.path.join(self.dir, default_file_path), "w", encoding="utf-8"
            ) as path:
                self.dir = self.dir
                print(self.dir, path)
        else:
            pass
