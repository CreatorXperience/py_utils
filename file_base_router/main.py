#!/home/codeknight/pysetup/.venv/bin/python3
"""

   FILE ROUTER:  CLI tool for file based routing

"""
from custom_parser import Parser
from custom_router import Router


parser = Parser()


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
        "default": "~/.router",
    }
)


@register
@register
def add_network_parser():
    subparser = parser.parser.add_subparsers(dest="func")
    network = subparser.add_parser("network")
    network.add_argument("-c", "--create", help="Create a new network")
    network.add_argument("-d", "--directory", help="Add a directory to the network")
    network.add_argument(
        "-s", "--show-net", help="Display all networks", action="store_true"
    )
    network.add_argument(
        "-S", "--show-dir", help="Display all directories", action="store_true"
    )


add_network_parser()
arguments = parser.parser.parse_args()

router = Router(arguments.change)
if arguments.func == "network":
    if arguments.create:
        print(arguments.create)
    if arguments.directory:
        print(arguments.directory)
router.monitor_dir()
