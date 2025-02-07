import dict2 as d


country_population= {
  "china": 143,
  "india": 136,
  "usa": 32,
  "pakistan": 21
}


def print_all():
  for k, v in country_population.items():
    print(k, v)


def add_country():
  country_name = input("country name")
  if country_name in country_population:
    print("country already exist")
    print(country_population[country_name])
  else:
    population = input('enter population')
    country_population[country_name] = population


def remove_country():
  country_name=input("enter country name")
  if country_name in country_population:
    del country_population[country_name]
    print_all()
  else:
    print("No such country")


def query_country():
  country_name = input("enter for query")
  print(country_population[country_name])

def remove_all():
  country_population.clear()
  print_all()

def main():
  inp= input("Enter what you want to do: ")
  if inp.lower() == "print":
    print_all()
  if inp.lower() == "add":
    add_country()
  if inp.lower() == "remove":
    remove_country()
  if inp.lower() == "query":
    query_country()
  if inp.lower() == "all":
    remove_all()
  else:
    d.main()

while 1:
  main()