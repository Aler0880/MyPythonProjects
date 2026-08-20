def count_stats():

    filename = input("Введите имя файла: ")

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        num_of_words = len(content.split())
        num_of_symbols = len(content)

    with open(filename, "r", encoding="utf-8") as f:
        num_of_str = sum(1 for line in f)

    stats = (num_of_str, num_of_words, num_of_symbols)
    print(content)
    print(stats)
    print("Количество строк: ", num_of_str)
    print("Количество слов: ", num_of_words)
    print("Количество символов: ", num_of_symbols)


count_stats()
