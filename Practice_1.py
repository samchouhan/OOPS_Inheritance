# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")

    def info(self):
        print(f"This animal's name is {self.name}")


# Child class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name)
        self.breed = breed

    # Method overriding
    def speak(self):
        print("Dog barks")

    def dog_info(self):
        print(f"{self.name} is a {self.breed}")


# Using the classes
a = Animal("GenericAnimal")
a.info()
a.speak()

print("------")

d = Dog("Buddy", "Labrador")
d.info()          # inherited method
d.speak()         # overridden method
d.dog_info()
