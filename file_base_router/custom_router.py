"""
    Instantiate a router object

"""

import time
import shutil
import os
import sys
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

    def on_modified(self, event: events.FileSystemEvent) -> None:
        return super().on_modified(event)

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
        super().on_created(event)

        for _, dest in enumerate(self.database.config["destinations"]):
            ismoved = self.move_file(dest, event.src_path)
            if ismoved:
                break

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
        super().on_moved(event)
        for _, dest in enumerate(self.database.config["destinations"]):
            ismoved = self.move_file(dest, event.src_path)
            if ismoved:
                break

    def move_file(self, dest_path, file_path):
        """
        moves file to destination

        """
        # shutil.move(file_path, path)
        # self.match_criteria(dest_path)
        req = list(
            filter(
                lambda val: val["Dest"] == dest_path, self.database.config["criteria"]
            )
        )

        if len(req) > 0:
            print(req)
            val = self.match_criteria(req[0], file_path)
            if val:
                print("all passsed")
                shutil.copy(file_path, dest_path)
                return True
        else:
            print("no criteria for this location")
            return False

    def match_criteria(self, requirement: dict, file_path: str):
        """
        Match Criteria

        """
        print(requirement)
        for attr, val in requirement.items():
            try:
                print(attr, val)
                self.comp_match(attr, val, file_path)
            except ValueError as ve:
                print(ve)
        return True

    def comp_match(self, item, value, file_path):
        """

        compares destination requirement with file stat

        """
        match item:
            case "ext":
                path = f"{file_path}"
                if path.endswith(f".{value}"):
                    print("extension rule passed ###################")
                else:
                    raise ValueError("extension rule failed xxxxxxxxxxxxxxxxxx ")

            case "Dest":
                print("Destinaton rule passed ################### ")

            case "min-size":
                file_stats = os.stat(file_path)
                if file_stats.st_size >= int(value):
                    print("minimum size  rule passed ################### ")
                else:
                    raise ValueError(
                        """minimum size rule doesn't meet requirements\nREASON: 
                        file size is lower than the requirement xxxxxxxxxxxxxxxxxx"""
                    )

            case "max-size":
                file_stats = os.stat(file_path)
                if file_stats.st_size <= int(value):
                    print("maximum size  rule passed ###################")
                else:
                    raise ValueError(
                        """maximum size rule doesn't meet requirements\nREASON: 
                        file size is higher than the requirement xxxxxxxxxxxxxxxxxx"""
                    )
            case "uid":
                f_stat = os.stat(file_path)
                uid = f_stat.st_uid
                if uid == int(value):
                    print("uid rule passed ################### ")
                else:
                    raise ValueError(
                        """uid rule failed xxxxxxxxxxxxxxxxxx\n
                            REASON: uid number doesn't meet requirement"""
                    )

            case "gid":
                f_stat = os.stat(file_path)
                gid = f_stat.st_gid
                if gid == int(value):
                    print("gid rule passed ################### ")
                else:
                    raise ValueError(
                        """gid rule failed xxxxxxxxxxxxxxxxxx\nREASON:
                        gid number doesn't meet requirement"""
                    )

            case _:
                print("falls in black hole")


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

    def move_file(self, dest_path, file_path):
        """
        moves file to destination

        """
        # shutil.move(file_path, path)
        # self.match_criteria(dest_path)
        req = list(
            filter(
                lambda val: val["Dest"] == dest_path, self.database.config["criteria"]
            )
        )

        if len(req) > 0:

            val = self.match_criteria(req[0], file_path)
            if val:
                print("all passsed")
                shutil.copy(file_path, dest_path)

    def match_criteria(self, requirement: dict, file_path: str):
        """
        Match Criteria

        """
        print(requirement)
        for attr, val in requirement.items():
            try:
                print(attr, val)
                self.comp_match(attr, val, file_path)
            except ValueError as ve:
                print(ve)
                sys.exit()
        return True

    def comp_match(self, item, value, file_path):
        """

        compares destination requirement with file stat

        """
        match item:
            case "ext":
                path = f"{file_path}"
                if path.endswith(f".{value}"):
                    print("extension rule passed ###################")
                else:
                    raise ValueError("extension rule failed xxxxxxxxxxxxxxxxxx ")

            case "Dest":
                print("Destinaton rule passed ################### ")

            case "min-size":
                file_stats = os.stat(file_path)
                if file_stats.st_size >= int(value):
                    print("minimum size  rule passed ################### ")
                else:
                    raise ValueError(
                        """minimum size rule doesn't meet requirements\nREASON: 
                        file size is lower than the requirement xxxxxxxxxxxxxxxxxx"""
                    )

            case "max-size":
                file_stats = os.stat(file_path)
                if file_stats.st_size <= int(value):
                    print("maximum size  rule passed ###################")
                else:
                    raise ValueError(
                        """maximum size rule doesn't meet requirements\nREASON: 
                        file size is higher than the requirement xxxxxxxxxxxxxxxxxx"""
                    )
            case "uid":
                f_stat = os.stat(file_path)
                uid = f_stat.st_uid
                if uid == int(value):
                    print("uid rule passed ################### ")
                else:
                    raise ValueError(
                        """uid rule failed xxxxxxxxxxxxxxxxxx\n
                            REASON: uid number doesn't meet requirement"""
                    )

            case "gid":
                f_stat = os.stat(file_path)
                gid = f_stat.st_gid
                if gid == int(value):
                    print("gid rule passed ################### ")
                else:
                    raise ValueError(
                        """gid rule failed xxxxxxxxxxxxxxxxxx\nREASON:
                        gid number doesn't meet requirement"""
                    )

            case _:
                print("falls in black hole")
