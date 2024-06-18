"""
    Instantiate a router object

"""

import time
from watchdog import observers
from watchdog import events
from config_database import Database


class WatchFSEventHandler(events.FileSystemEventHandler):
    """
    Extends watchdog event FileSystemHandler

    """

    def __init__(self, database: Database):
        super()
        self.database = database

    def on_created(self, event: events.FileSystemEvent) -> None:
        if event.is_directory:
            print(f"directory created ##### {event.src_path}")
            self.database.config = {
                **self.database.config,
                "d_count": self.database.config["d_count"] + 1,
            }
        else:
            print(f"file created ##### {event.src_path}")
            self.database.config = {
                **self.database.config,
                "f_count": self.database.config["f_count"] + 1,
            }
        self.database.update_config()
        return super().on_created(event)

    def on_deleted(self, event: events.FileSystemEvent) -> None:
        print(f"file deleted ######## {event.src_path}")
        if event.is_directory:
            self.database.config = {
                **self.database.config,
                "d_count": self.database.config["d_count"] - 1,
            }
        else:
            self.database.config = {
                **self.database.config,
                "f_count": self.database.config["f_count"] - 1,
            }

        self.database.update_config()
        return super().on_deleted(event)


class Router:
    """

    Instantaiate a router object

    """

    def __init__(self, database: Database):
        self.database = database
        # self.dir_path = database.config("database")

    def monitor_dir(self):
        """
        sets default folder for routing files

        """
        observer = observers.Observer()
        event_handler = WatchFSEventHandler(self.database)
        obj = self.database.config
        observer.schedule(event_handler, path=obj["database"], recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
