import json
from pprint import pprint
file_path="./app.js"
with open(file_path, "r") as open_file:
    text = open_file.readlines()
print(open_file.closed)

pdf_path = "./service-policy.json"

with open(pdf_path, mode="r") as open_pdf:
    policy = json.loads(open_pdf)
    pprint(policy)