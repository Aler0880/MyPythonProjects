filename = input("Введите имя файла: ")


def count_stats(filename):

    try:
        with open(filename, "r", encoding="utf-8") as f:
            num_of_str = 0
            num_of_words = 0
            num_of_symbols = 0
            for line in f:
                num_of_str += 1
                num_of_words += len(line.split())
                num_of_symbols += len(line)
            if num_of_symbols == 0:
                return "Файл пуст"

        return (filename, num_of_str, num_of_words, num_of_symbols)

    except FileNotFoundError:
        return "Файл не найден"


with open("result.txt", "w", encoding="utf-8") as f:
    result = count_stats(filename)
    if type(result) == tuple:
        f.write(
            f"Файл: {result[0]}\nСтрок: {result[1]}\nСлов: {result[2]}\nСимволов: {result[3]}"
        )
    else:
        f.write(str(result))

with open("result.txt", "r", encoding="utf-8") as f:
    print(f.read())
