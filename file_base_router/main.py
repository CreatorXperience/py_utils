#!/home/codeknight/pysetup/.venv/bin/python3
"""

   FILE ROUTER:  CLI tool for file based routing

"""

from os import path
from pprint import pprint
import shutil
from custom_parser import Parser
from config_database import Database
from custom_router import Router


parser = Parser()
subparser = parser.parser.add_subparsers(dest="func")

register = parser.use_parser()


@register
def add_argument(option):
    """

    Add's custom argument to parser object

    """

    parser_object = parser.parser.add_argument(
        option["opt"], option["abbr"], help=option["help"], default=option["default"]
    )
    return parser_object


add_argument(
    {
        "opt": "-c",
        "abbr": "--change",
        "help": "Create router database",
        "default": path.expanduser("~/.router"),
    }
)


@register
def action():
    """
    Perform an action on file e.g move a file

    """
    act = subparser.add_parser("action")
    act.add_argument(
        "-m",
        "--move_to",
        help="Move Content to destination",
    )

    act.add_argument(
        "-r",
        "--retrieve",
        help="retrieve file from destination",
    )
    act.add_argument("file", help="File to move")


@register
def bind_criteria():
    """

    Bind criteria with destination e.g defines the critieria all

    files must conform to before routing files to destination

    """
    c_parser = subparser.add_parser("criteria")
    c_parser.add_argument(
        "-n", "--new", help="create a new criteria", action="store_true"
    )
    c_parser.add_argument(
        "ctype",
        help="criteria type",
        choices=["ext", "min-size", "max-size", "uid", "gid"],
    )

    c_parser.add_argument("cvalue", help="value for your type")
    c_parser.add_argument("destination", help="specify an existing destination ")


# call parsers
# add_dest_parser()
action()
bind_criteria()


arguments = parser.parser.parse_args()

database = Database(arguments.change)
database.create_database()

router = Router(database)

if arguments.func == "action":
    if path.exists(path.abspath(arguments.file)):
        try:
            shutil.copy(path.abspath(arguments.file), dst=database.config["database"])
            move_event = router.move_event(path.abspath(arguments.file))
            router.fs_handler.on_moved(move_event)
        except shutil.Error as Fe:
            print("file already exists")
    if arguments.move_to:
        router.move_file(arguments.move_to, arguments.file)
    if arguments.retrieve:
        pass
        # router.retrieve(arguments.retrieve, arguments.file)

elif arguments.func == "criteria":
    if arguments.new:
        pass
    if arguments.ctype and arguments.destination and arguments.cvalue:
        obj = list(
            filter(
                lambda val: val["Dest"] == arguments.destination,
                database.config["criteria"],
            )
        )
        dest_clone = list(
            filter(
                lambda val: val["Dest"] != arguments.destination,
                database.config["criteria"],
            )
        )

        if len(obj) > 0:
            obj[0][arguments.ctype] = arguments.cvalue
            database.config = {**database.config, "criteria": [*dest_clone, obj[0]]}
            pprint("okay")
        elif len(obj) == 0:
            new_obj = {arguments.ctype: arguments.cvalue, "Dest": arguments.destination}
            database.config = {**database.config, "criteria": [*dest_clone, new_obj]}

        print(arguments.ctype)
    if arguments.destination:
        if path.exists(arguments.destination):
            dest_clone = list(
                filter(
                    lambda val: val != arguments.destination,
                    database.config["destinations"],
                )
            )
            database.config = {
                **database.config,
                "destinations": [*dest_clone, arguments.destination],
            }
            database.update_config()
            pprint(database.config)

router.monitor_dir()
