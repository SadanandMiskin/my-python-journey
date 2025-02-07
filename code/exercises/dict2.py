stocks = {
  "info": [600, 630, 620],
  "ril": [1430, 1490, 1567],
  "mtl": [234, 180, 160]
}


def print_avg():
  for key in stocks:
    sum = 0
    # print(key)
    # print(len(stocks[key]))
    for i in range(len(stocks[key])):
      sum = sum + stocks[key][i]
    print(key , " ==> ", stocks[key] , " ==> avg: ", round(sum/len(stocks[key]), 2))

def add_stock():
  stock_name = input("enter stock name")
  stock_val = int(input("enter val"))
  if stock_name in stocks:
    # print("stock already exists")
    stocks[stock_name].append(stock_val)
  else:
    stocks[stock_name] = [stock_val]
  print(stocks)


def main():
  inp=input("enter option")
  if inp == "print":
    print_avg()
  if inp =="add":
    add_stock()

while 1:
  main()