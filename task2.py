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
                return print("Файл пуст")

        stats = (num_of_str, num_of_words, num_of_symbols)

        return stats

    except FileNotFoundError:
        print("Файл не найден")


count_stats(filename)

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(str(count_stats(filename)))
