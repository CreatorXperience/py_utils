"""
    Instantiate a router object

"""

import time
from watchdog import observers
from watchdog import events


class WatchFSEventHandler(events.FileSystemEventHandler):
    """
    Extends watchdog event FileSystemHandler

    """

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"file created {event.src_path}")


class Router:
    """

    Instantaiate a router object

    """

    def __init__(self, path):
        self.dir_path = path

    def monitor_dir(self):
        """
        sets default folder for routing files

        """
        observer = observers.Observer()
        event_handler = WatchFSEventHandler()
        observer.schedule(event_handler, path=self.dir_path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
