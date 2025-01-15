#py lambda function -> defining unnamed small functions in a single line
# specially fot the short operations

square = lambda x: x *2
print(square(2))

numbers = [1,2,3,4,5]
squared = map(lambda x: x*2, numbers)
print(list(squared))

filtered = list(filter(lambda x : x > 3 , list(squared)))
print(filtered)


# this code does not works brcause the iterator map is consumned in print() at starting, hence first we need to convert it to list in the start become consuming
# the iterator squared is exhausted in print(list(map)) and hence cannot be used for next iterator
# Hence we need to convert the squared iterator to list

numbers = [1,2,3,4,5]
squared = list(map(lambda x: x*2, numbers))
print(list(squared))

filtered = list(filter(lambda x : x > 3 , list(squared)))
print(filtered)