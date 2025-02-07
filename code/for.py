# marks=[12,31,312,41,413,41,413]

# for i in range(0, len(marks)-5):
#   print(marks)

key_loc="chair"
locations=["garbage", "room", "chair", "closet"]
for i in range(len(locations)):
  if locations[i] == key_loc:
    print("found at ", i)
    break
  else:
    print("not present")

for i in range(5):
  if i%2 == 0:
    print(i*i)
  else:
    continue