import json
from pprint import pprint

data = dict()
with open("newsafr.json", encoding="utf-8") as file:
    data = json.loads(file.read())

pprint(data, width=100)

