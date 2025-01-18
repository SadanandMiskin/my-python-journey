class Animal:

  # initialising a constructor, self is nothing but 'this' , but we need to explicitly pass it as param
  #  It explicitly requires self as the first parameter in all instance methods to refer to the object itself.
  def __init__(self, name):
    self.name=name
  def speak(self):
    return f"{self.name} makes a sound"

# this is how we inherit 'Animal' in py
class Dog(Animal):
  def speak(self):
    return f"{self.name} barks"


generic_animal = Animal("Generic Animal")

dog = Dog("buddy")
print(generic_animal.speak())
print(dog.speak())
