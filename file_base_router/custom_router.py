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
        self.config_obj = self.database.config

    def on_created(self, event: events.FileSystemEvent) -> None:
        if event.is_directory:
            print(f"directory created ##### {event.src_path}")
            self.config_obj = {
                **self.config_obj,
                "d_count": self.config_obj["d_count"] + 1,
            }
        else:
            print(f"file created ##### {event.src_path}")
            self.config_obj = {
                **self.config_obj,
                "f_count": self.config_obj["f_count"] + 1,
            }
        self.database.update_config()
        return super().on_created(event)

    def on_deleted(self, event: events.FileSystemEvent) -> None:
        print(f"file deleted ######## {event.src_path}")
        if event.is_directory:
            self.config_obj = {
                **self.config_obj,
                "d_count": self.config_obj["d_count"] - 1,
            }
        else:
            self.config_obj = {
                **self.config_obj,
                "f_count": self.config_obj["f_count"] - 1,
            }

        self.database.update_config()
        return super().on_deleted(event)

    def on_moved(self, event: events.FileSystemEvent) -> None:
        print(f"file moved ######## {event.src_path}")
        if event.is_directory:
            self.config_obj = {
                **self.config_obj,
                "d_count": self.config_obj["d_count"] + 1,
            }
        else:
            self.config_obj = {
                **self.config_obj,
                "f_count": self.config_obj["f_count"] + 1,
            }
        self.database.update_config()
        return super().on_moved(event)


class Router:
    """

    Instantaiate a router object

    """

    def __init__(self, database: Database):
        self.database = database
        self.move_event = events.FileMovedEvent
        self.fs_handler = WatchFSEventHandler(self.database)
        # self.dir_path = database.config("database")

    def monitor_dir(self):
        """
        sets default folder for routing files

        """
        observer = observers.Observer()

        obj = self.database.config
        observer.schedule(self.fs_handler, path=obj["database"], recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
