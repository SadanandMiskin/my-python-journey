telephone_dict= {
  "tom": 3434134,
  "john": 13234
}
telephone_dict["tom"] = "asdad"

# del telephone_dict["tom"]
print(telephone_dict["tom"])


for key in telephone_dict:
  print(key, telephone_dict[key])

for k,v in telephone_dict.items():
  print(k, v)

print("d" in telephone_dict)

telephone_dict.clear()