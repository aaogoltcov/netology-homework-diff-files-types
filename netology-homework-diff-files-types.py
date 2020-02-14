import json
from pprint import pprint

data = dict()
with open("newsafr.json", encoding="utf-8") as file:
    data = json.loads(file.read())

descriptions = data['rss']['channel']['items']
# pprint(descriptions)
# pprint(descriptions[0])

list_of_words = list()
news_count = 0
while news_count < len(descriptions):
    full_string = str()
    for description in descriptions:
        add_string = str(description['description'])
        # if not full_string:
        #     full_string = add_string
        # else:
        #     full_string = full_string + ' ' + add_string
        add_string = add_string.split()
        for word in add_string:
            if len(word) > 6:
                list_of_words.append(word)
        # print(description['description'])
    # pprint(descriptions[news_count])
    news_count += 1
# pprint(full_string)
# full_string = full_string.split()
# pprint(full_string)
print(list_of_words)

# for description in data['rss']['channel']['items'][0]:
#     for key, value in description:
#         if key == 'description':
#             pprint(value)
# pprint(data['description'], width=100)
# pprint(data['rss']['channel']['items'], width=100)
