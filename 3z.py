while True:
    a = input("введите слово ")
    if a == "stop":
        break
    if "ф" or "Ф" in a:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

