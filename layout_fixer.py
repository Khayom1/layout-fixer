ru_to_en = {
    'й':'q', 'ц':'w', 'у':'e', 'к':'r', 'е':'t', 'н':'y', 'г':'u', 'ш':'i', 'щ':'o', 'з':'p', 'х':'[', 'ъ':']',
    'ф':'a', 'ы':'s', 'в':'d', 'а':'f', 'п':'g', 'р':'h', 'о':'j', 'л':'k', 'д':'l', 'ж':';', 'э':"'",
    'я':'z', 'ч':'x', 'с':'c', 'м':'v', 'и':'b', 'т':'n', 'ь':'m', 'б':',', 'ю':'.',
    'Й':'Q', 'Ц':'W', 'У':'E', 'К':'R', 'Е':'T', 'Н':'Y', 'Г':'U', 'Ш':'I', 'Щ':'O', 'З':'P', 'Х':'{', 'Ъ':'}',
    'Ф':'A', 'Ы':'S', 'В':'D', 'А':'F', 'П':'G', 'Р':'H', 'О':'J', 'Л':'K', 'Д':'L', 'Ж':':', 'Э':'"',
    'Я':'Z', 'Ч':'X', 'С':'C', 'М':'V', 'И':'B', 'Т':'N', 'Ь':'M', 'Б':'<', 'Ю':'>'
}

en_to_ru = {v: k for k, v in ru_to_en.items()}

def convert(text, direction):
    table = ru_to_en if direction == "1" else en_to_ru
    return ''.join(table.get(c, c) for c in text)

def main():
    print("\n=== Layout Fixer ===")
    print("1. Russian → English")
    print("2. English → Russian")
    print("0. Exit\n")

    while True:
        choice = input("Choose an option (1 / 2 / 0): ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        if choice not in ("1", "2"):
            print("❌ Please choose 1, 2, or 0!\n")
            continue
        text = input("\nEnter the text (then press Enter): ")
        result = convert(text, choice)
        print("\n--- Result ---")
        print(result)
        print("-" * 40 + "\n")

if __name__ == "__main__":
    main()
