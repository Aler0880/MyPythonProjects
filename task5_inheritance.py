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
        return(f"Вид: {self.species}\nИмя: {self.name}\nВозраст: {self.age}")

    def __str__(self):
        return f"Вид: {self.species}; Имя: {self.name}; Возраст: {self.age}"


class Dog(Animal):

    def make_sound(self):
        return("Гав-гав")

    def fetch(self):
        return(f"{self.name} несёт мяч")

    def __str__(self):
            return f"Имя: {self.name}; Возраст: {self.age}"


class Cat(Animal):

    def make_sound(self):
        return("Мяу")

    def murr(self):
        return(f"{self.name} мурлычет...")

    def __str__(self):
                return f"Имя: {self.name}; Возраст: {self.age}"

dog = Dog("собака", input("Имя собаки: "), input("Возраст собаки: "))
cat = Cat("кошка", input("Имя кошки: "), input("Возраст кошки: "))
bobr = Animal("бобер", input("Имя бобра: "), input("Возраст бобра: "))
animal_sound = input("Какой звук издаёт бобёр?: ")
animal_doing = input("Что делает бобёр?: ")

print()
print(dog)
print('Издаёт звук: ', dog.make_sound())
print('Что делает: ', dog.fetch())
print()
print(cat)
print('Издаёт звук: ', cat.make_sound())
print('Что делает: ', cat.murr())
print()
print(bobr)
print("Бобёр издаёт звук: ", bobr.make_sound())
print('Бобёр', bobr.make_something())
