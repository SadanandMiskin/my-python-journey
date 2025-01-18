class Bird:
  def fly(self):
    return "Birds Fly"

class Penguin:
  def fly(self):
    return "Penguin cannot fly"

def get_fly_info(bird):
  print(bird.fly())

parrot = Bird()
penguin = Penguin()

get_fly_info(parrot)
get_fly_info(penguin)



class Product:
  def __init__(self, a, b, c=None):
     self.a = a
     self.b = b
     self.c= c

  # def product(self):
  #   return self.a * self.b

  def product(self):
    if self.c is not None:
      return self.a*self.b*self.c
    else:
      return self.a * self.b

get_product = Product(1,2)
print(get_product.product())


