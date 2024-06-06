import json
import pathlib
from pprint import pprint
import os
if __name__ == "__main__":
    file_path="./app.js"
    with open(file_path, "r") as open_file:
        text = open_file.readlines()
    print(open_file.closed)

    # pdf_path = "./service-policy.json"

    # with open(pdf_path, mode="w") as open_pdf:
    #     policy = json.loads(open_pdf)
    #     pprint(policy)


    def walk_through_shadow_of_dirs(parent_dir):
        if not os.path.isdir(parent_dir):
            print(f"{parent_dir} is not a directory")
        else:
            childs =  os.listdir(parent_dir)
            for child in childs:
                fpath = os.path.join(parent_dir,child)
                print(fpath)
                if not os.path.isdir(fpath):
                    print(fpath)
                    size = os.path.getsize(fpath)
                    atime = os.path.getatime(fpath)
                    print(f"File: {fpath} ")
                    print(f"Size: {size}")
                    print(f"Accessed-time: {atime}")
                elif os.path.isdir(fpath):
                    walk_through_shadow_of_dirs(fpath)


    walk_through_shadow_of_dirs("/home/codeknight/cookie")

def run():
    print("initializing")
    print("completing")
    print("finished")