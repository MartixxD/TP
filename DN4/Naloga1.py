import json

podatki = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

json_object = json.dumps(podatki, indent = 4) 
print(json_object)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)