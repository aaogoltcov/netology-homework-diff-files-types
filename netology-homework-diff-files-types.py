import json
import operator
from collections import Counter
import xml.etree.ElementTree as ET


def first_10_words(descriptions):
    list_of_words = list()
    words = str()
    for description in descriptions:
        # if type(description) == types.dict "<class 'dict'>":
        if isinstance(description, dict):
            words = str(description['description'])
            words = words.lower()
            words = words.split()
        # elif type(description) == "<class 'xml.etree.ElementTree.Element'>":
        else:
            words = str(description.find("description").text)
            words = words.lower()
            words = words.split()
        for word in words:
            if len(word) > 6:
                list_of_words.append(word)
    list_of_words = Counter(list_of_words)
    list_of_words = sorted(list_of_words.items(), key=operator.itemgetter(1), reverse=True)
    first_10_count = 0
    for word in list_of_words:
        if first_10_count == 10:
            break
        else:
            print(f'{first_10_count + 1} место: слово "{word[0]}" повторялось {word[1]} раз')
            first_10_count += 1


print('\nЧтение JSON файл:')
data = dict()
with open("newsafr.json", encoding="utf-8") as file:
    data = json.loads(file.read())
descriptions = data['rss']['channel']['items']
first_10_words(descriptions)

print('\nЧтение XML файла:')
data = ET.parse("newsafr.xml")
data_root = data.getroot()
descriptions = data_root.findall(r"channel/item")
first_10_words(descriptions)