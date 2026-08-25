# Работа с API (requests, JSON)

import requests
import json

try:
    rep = input("Введите название репозитория: ")
    url = f"https://api.github.com/repos/python/{rep}"  # "https://api.github.com/repos/python/cpython"

    response = requests.get(url)

    if response.status_code == 404:
        print("Репозиторий не найден!")
        with open("result3.txt", "w", encoding="utf-8") as f:
            f.write("Репозиторий не найден!")

    # Можно выйти или спросить другой репозиторий
    else:
        # try:
        data = response.json()
        # except json.JSONDecodeError:
        # print("Ответ не является JSON")

        name = data.get("name")
        stars = data.get("stargazers_count")
        forks = data.get("forks_count")
        updated = data.get("updated_at")
        # nonex = data.get("nonex_key")

        print("Название:", name)
        print("Звёзд:", stars)
        print("Форков:", forks)
        print("Обновлён:", updated)
        with open("result3.txt", "w", encoding="utf-8") as f:
            f.write(f"Название: {name}\nЗвёзд: {stars}"
                    f"\nФорков: {forks}\nОбновлён: {updated}")
        # print("Нет такого: ", nonex)

except requests.exceptions.RequestException:

    print("Ошибка связи")
    with open("result3.txt", "w", encoding="utf-8") as f:
        f.write("Ошибка связи")

# print(response.status_code)

# print(response.text[:500])

# print(type(data))

# print(*data.keys(), sep='\n')
