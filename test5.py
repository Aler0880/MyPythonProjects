class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):

    def color(self):
        return f"black"

    def __str__(self):
        return f"{self.name}, {self.age}, {self.color()}"


my_dog = Dog("Reks", 5)

print(my_dog)
