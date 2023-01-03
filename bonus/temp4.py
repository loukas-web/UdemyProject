import json

with open("temp4.json", "r") as file:
    data = file.read()

info = json.loads(data)

print(info)
print(info["address"]["city"])
print(info["phoneNumbers"][0]["number"])
