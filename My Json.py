import json

data = '{"var1":"Avijit","var2":"99"}'
parsed = json.loads(data)
print(parsed)
print(parsed['var1'])
print(type(parsed))

data2 = {
    "name": "Avijit Samanta",
    "language": ['C', 'C++', 'JAVA', 'Python', 'Android'],
    "fridge": ('roti', 540),
    "marriage": False
}
jsComp = json.dumps(data2)
print(jsComp)
