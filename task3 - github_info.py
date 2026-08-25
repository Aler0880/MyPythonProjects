# Работа с API (requests, JSON)

import requests

url = "https://api.github.com/repos/python/cpython"

response = requests.get(url)

data = response.json()

name = data.get("name")
stars = data.get("stargazers_count")
forks = data.get("forks_count")
updated = data.get("updated_at")
nonex = data.get("nonex_key")

print("Название:", name)
print("Звёзд:", stars)
print("Форков:", forks)
print("Обновлён:", updated)
print("Нет такого: ", nonex)

# print(response.status_code)

# print(response.text[:500])

# print(type(data))

# print(*data.keys(), sep='\n')
