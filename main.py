import json

f = open('https://raw.githubusercontent.com/ryczek02/Polskie-jednostki-administracyjne/master/miasta.json', encoding='utf-8')

data = json.load(f)

print(data)