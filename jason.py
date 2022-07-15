import json
f = open('sotcks.json', 'r', encoding='utf-8')
kospi = json.load(f)
print(kospi['stocks'][0])

