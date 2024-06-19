#!/home/codeknight/pysetup/.venv/bin/python3
"""

   FILE ROUTER:  CLI tool for file based routing

"""

from os import path
import shutil
import sys
from custom_parser import Parser
from config_database import Database
from custom_router import Router
from pprint import pprint


parser = Parser()
subparser = parser.parser.add_subparsers(dest="func")

register = parser.use_parser()


@register
def add_argument(option):
    """

    Add's custom argument to parser object

    """

    obj = parser.parser.add_argument(
        option["opt"], option["abbr"], help=option["help"], default=option["default"]
    )
    return obj


add_argument(
    {
        "opt": "-c",
        "abbr": "--change",
        "help": "Create router database",
        "default": path.expanduser("~/.router"),
    }
)


@register
def add_network_parser():
    """
    Add's network  Subparser to parser object
    """
    network = subparser.add_parser("destination")
    network.add_argument("-c", "--create", help="Create a new destination")
    network.add_argument(
        "-s", "--show-net", help="Display all networks", action="store_true"
    )
    network.add_argument(
        "-S", "--show-dir", help="Display all directories", action="store_true"
    )


@register
def action():
    """
    Perform an action on file e.g move a file

    """
    act = subparser.add_parser("action")
    act.add_argument("-m", "--move", help="Move Content to dabase", action="store_true")
    act.add_argument("file", help="File to move")


add_network_parser()
action()
arguments = parser.parser.parse_args()

database = Database(arguments.change)
database.create_database()

router = Router(database)

if arguments.func == "destination":
    if arguments.create:
        db_clone = database.config["destinations"]
        if path.exists(arguments.create):
            for index, item in enumerate(database.config["destinations"]):

                if item == arguments.create:
                    print("path already exist")
                    db_clone.pop(index)
                    print(db_clone)
                    database.config = {
                        **database.config,
                        "destinations": db_clone,
                    }

            database.config = {
                **database.config,
                "destinations": [*database.config["destinations"], arguments.create],
            }
            pprint(database.config)
            database.update_config()
        # net_path = path.join(database.config["networks"], arguments.create)
        # print(arguments.create)
        # os.mkdir(net_path)

    # if arguments.directory:
    #     net = input("destination: ")
    #     net_path = path.join(database.config["destination"], net)
    #     if os.path.exists(path.join(path.dirname(net_path), net)):
    #         print("destination exist")
    #         os.mkdir(
    #             path.join(path.dirname(net_path), path.join(net, arguments.directory))
    #         )

    #     print(arguments.directory)

elif arguments.func == "action":
    if path.exists(path.abspath(arguments.file)):
        print(database.config)
        try:
            shutil.move(path.abspath(arguments.file), dst=database.config["database"])
            move_event = router.move_event(path.abspath(arguments.file))
            router.fs_handler.on_moved(move_event)
        except shutil.Error as Fe:
            print("file already exists")


router.monitor_dir()
