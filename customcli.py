#!/home/codeknight/pysetup/.venv/bin/python
from fire import Fire
# import argparse

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Top Level command")
#     parser.add_argument("-t", "--twice", help="Print twice", action="store_true")
#     subparser = parser.add_subparsers(dest="func")
#     react = subparser.add_parser("react-app")
#     react.add_argument("renderer", choices=["list", "table"])
#     react.add_argument("-c", "--check", help="check react app", action="store_true")
#     angular = subparser.add_parser("angular")
#     angular.add_argument("-c", "--check", help="check angular app", action="store_true")
#     args = parser.parse_args()
#     if args.twice:
#         yo= [print("prints twice") for x in range(0,2)]
#     if args.func == "react-app":
#         if args.check:
#             print("good working react app")
#         elif args.renderer == "list":
#             print(["react-dom", "react-fiber"])
#         elif args.renderer == "table":
#             print("no table for this data")
#         else:
#             print("bad app")
#     elif args.func == "angular":
#         if args.check:
#             print("good working angular app")
#         else:
#             print("Garbaage command check help with --help")

class Git():
    def branch(self):
        br = "branch1"
        print(br)

    def repository(self):
        repo = "front-end app"
        print(repo)


def enc(passwd):
    print(f"{passwd}")

class Sail():
    def __init__(self):
        self.enc = enc
        self.git = Git

if __name__ == "__main__":
    Fire(Sail)