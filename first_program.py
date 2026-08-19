n = int(input("Введите число 'n': "))
l = list(range(1, n + 1))
print(l)

l1 = [i**2 for i in l if i % 2 == 0]
print("Квадраты четных чисел до n: ", l1)
