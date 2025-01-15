import json


# dictionary to json string
person_dict = {"name": "sadanand" , "age": 21}
person_json = json.dumps(person_dict)
print(person_json)

# json string to dictionary
person_dict = json.loads(person_json)
print(person_dict)

print(type(person_dict) , type(person_json))

# json parse is similar as of JS like  JSON.stringify()->json to string,   JSON.parse() -> json string to json object