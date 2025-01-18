def greet(name="world" , *args , **kwargs):
  print(f"Hello {name}") #if argument is present then it overwrites the default "World"
  print(args) # combine the arguments to form a tupple (1,2) -> arguments
  print(kwargs) #combines the arguments to forma a dictionary -> keywordArguments

greet("Sads" , 1,2, color = "blue" , age=30, )