class BankAccount:
    def __init__(self, initial_balance=0):
        # Проверяем, что начальный баланс не отрицательный
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.__balance = initial_balance

    @property
    def balance(self):
        """Свойство для получения баланса (используем без скобок)"""
        return self.__balance

    def set_initial_balance(self, amount):
        """Устанавливает новый начальный баланс (заменяет текущий)"""
        if amount < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.__balance = amount

    def add(self, amount):
        """Пополняет счёт на положительную сумму, только если баланс не отрицательный"""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        if self.__balance < 0:
            raise ValueError("Баланс отрицательный – пополнить нельзя")
        self.__balance += amount

    def withdraw(self, amount):
        """Снимает сумму, если она положительна и не превышает баланс"""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount


def enter():
    # Создаём счёт с нулевым балансом
    acc = BankAccount(0)

    while True:
        # Используем свойство balance без скобок
        command = input(
            f"'Снять', 'Пополнить', 'Изменить баланс', 'Выход' (текущий баланс: {acc.balance}): "
        )

        if command == "Выход":
            break

        elif command == "Изменить баланс":
            while True:
                try:
                    new_balance = int(input("Введите новый начальный баланс: "))
                    acc.set_initial_balance(new_balance)
                    print(f"Баланс установлен: {acc.balance}")
                    break
                except ValueError as e:
                    print(f"Ошибка: {e}. Попробуйте снова.")

        elif command == "Пополнить":
            while True:
                try:
                    amount = int(input("Сумма пополнения: "))
                    acc.add(amount)
                    print(f"Текущий баланс: {acc.balance}")
                    break
                except ValueError as e:
                    print(f"Ошибка: {e}. Попробуйте снова.")

        elif command == "Снять":
            while True:
                try:
                    amount = int(input("Сумма снятия: "))
                    acc.withdraw(amount)
                    print(f"Текущий баланс: {acc.balance}")
                    break
                except ValueError as e:
                    print(f"Ошибка: {e}. Попробуйте снова.")

        else:
            print("Неверная команда. Пожалуйста, выберите из предложенных.")


if __name__ == "__main__":
    enter()