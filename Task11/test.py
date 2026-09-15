name = "Толстой"
for enc in ["cp866", "cp1251", "utf-8", "mbcs"]:
    try:
        encoded = name.encode(enc)
        print(f"{enc}: {encoded!r}")
    except Exception as e:
        print(f"{enc}: ошибка {e}")
