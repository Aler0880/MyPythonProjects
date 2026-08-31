class Animal:

    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

    def make_sound(self):
        return animal_sound

    def make_something(self):
        return animal_doing

    def info(self):
        return f"Вид: {self.species}\nИмя: {self.name}\nВозраст: {self.age}"


class Dog(Animal):

    def make_sound(self):
        return "Гав-гав"

    def fetch(self):
        return f"{self.name} несёт мяч"


class Cat(Animal):

    def make_sound(self):
        return "Мяу"

    def murr(self):
        return f"{self.name} мурлычет..."


dog = Dog("собака", input("Имя собаки: "), input("Возраст собаки: "))
cat = Cat("кошка", input("Имя кошки: "), input("Возраст кошки: "))
any_species = input("Вид другого животного: ")
any_animal = Animal(
    any_species, input(f"Имя {any_species}а: "), input(f"Возраст {any_species}а: ")
)
animal_sound = input(f"Какой звук издаёт {any_species}: ")
animal_doing = input(f"Что делает {any_species}?: ")

print()
print(dog)
print("Издаёт звук: ", dog.make_sound())
print("Что делает: ", dog.fetch())
print(dog.info())
print("Издаёт звук: ", dog.make_sound())
print("Что делает: ", dog.fetch())
print()
print(cat)
print("Издаёт звук: ", cat.make_sound())
print("Что делает: ", cat.murr())
print(cat.info())
print("Издаёт звук: ", cat.make_sound())
print("Что делает: ", cat.murr())
print()
print(any_animal.info())
print(f"{any_species} издаёт звук: ", any_animal.make_sound())
print(any_animal.species, any_animal.make_something())
