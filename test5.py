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


#########################################################################################################################


# class Square:
#     def __init__(self, side):

#         self.side = side

#     @property
#     def area(self):
#         return self.side**2

#     @property
#     def perimeter(self):
#         return self.side * 4


# Sq1 = Square(int(input("Введите сторону квадрата: ")))

# print(f"Площадь: {Sq1.area:.2f}")
# print(f"Периметр: {Sq1.perimeter:.2f}")

# Sq1.side = int(input("Введите сторону квадрата: "))

# print(f"Площадь: {Sq1.area:.2f}")
# print(f"Периметр: {Sq1.perimeter:.2f}")


#########################################################################################################################


class BankAccount:
    def __init__(self, __balance):
        self.__balance = __balance

    def add(self, add_amount):

        try:
            if self.__balance < 0:
                raise ValueError("Баланс отрицательный - пополнить нельзя")

            self.__balance = self.__balance + add_amount
        except:
            self.__balance = int(input("Введите положительный начальный баланс: "))

    def withdraw(self, withdraw_amount):

        try:
            if withdraw_amount <= 0:
                raise ValueError("Cумма должна быть положительной")
            if withdraw_amount <= self.__balance:
                self.__balance = self.__balance - withdraw_amount
                return
            if withdraw_amount > self.__balance:
                raise ValueError("Недостаточно средств")
        except:
            acc.withdraw(int(input("Введите корректную сумму: ")))

    # @property
    def balance(self):
        return self.__balance

    
    def initial_balance(self, initial_amount):
        self.initial_amount = initial_amount
        return initial_amount


acc = BankAccount(0)


def enter():

    while True:

        enter = input(
            f"'Снять', 'Пополнить', 'Изменить баланс ({acc.balance()})', 'Выход': "
        )
        if enter != "Выход" and enter == "Изменить баланс":
            initial_balance(int(input("Начальный баланс:")))

            print("Текущий баланс: ", initial_balance())

        elif enter == "Пополнить":
            acc.add(int(input("Сумма пополнения: ")))

            print("Текущий баланс: ", acc.balance())

        elif enter == "Снять":
            acc.withdraw(int(input("Сумма снятия: ")))

            print("Текущий баланс: ", acc.balance())

        elif enter == "Выход":
            break
        else:
            print("Сделайте корректный ввод: ")


enter()
