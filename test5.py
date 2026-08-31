# class Длина:
#     def __init__(self, метры):
#         self._метры = метры

#     @property
#     def метры(self):
#         return self._метры

#     @метры.setter
#     def метры(self, значение):
#         self._метры = значение

#     @property
#     def сантиметры(self):
#         return self._метры * 100

#     @сантиметры.setter
#     def сантиметры(self, значение):
#         self._метры = значение / 100

# d = Длина(2)          # 2 метра
# print(d.сантиметры)   # 200
# d.сантиметры = 150    # устанавливаем 150 см
# print(d.метры)        # 1.5


class Square:
    def __init__(self, side):

        self.side = side

    @property
    def area(self):
        return self.side**2

    @property
    def perimeter(self):
        return self.side * 4


Sq1 = Square(int(input("Введите сторону квадрата: ")))

print(f"Площадь: {Sq1.area:.2f}")
print(f"Периметр: {Sq1.perimeter:.2f}")

Sq1.side = int(input("Введите сторону квадрата: "))

print(f"Площадь: {Sq1.area:.2f}")
print(f"Периметр: {Sq1.perimeter:.2f}")
