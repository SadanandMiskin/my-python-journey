book={}
book['tom'] = {
  "name": "tom",
  "address": "London",
  "Phone": 13124323221
}

book['bob'] = {
  "name": "bob",
  "address": "New York",
  "Phone": 939393993
}


import json
print(json.dumps(book)) # to string
s=json.dumps(book)
print(book)


# with open("/home/sads/Desktop/data-science/book.txt" , 'w') as f:
#   f.write(s)


f= open("/home/sads/Desktop/data-science/book.txt" , 'w')
f.write(s)

for person in book:
  print(book[person]["address"])

# f= open("/home/sads/Desktop/data-science/book.txt" , 'r')
# s= f.read()
# print(s)