print("hello")


for i in range(10):
  print(i)


# Liat: Similar to array
my_list = [1, 2, "apple"]
print(my_list)

print(my_list.pop(1))
print(my_list)

# Tupples: Immutable arrays
my_tupple = (1, 2, "apple")

# Sets: Holds Unique elements
my_set = {1,2,3,2} # Output: {1,2,3}
print(my_set)   # In JS: const set  = new Set({1,2,3})

# Dictionaries
my_dict = {"name": "SadanandMiskin" , "age": 21}
# In python the keys are string types where as in js keys are non-string types

# Condition
age = 18
if age < 20:
  print("Younger")
elif age == 20:
  print("20 Age")
else:
  print("Elder")



# Loops
for i in range(10):
  print(i)

i = 1
while i == 10:
  print(i)
  i += 1


name = input("name")
print(name)
