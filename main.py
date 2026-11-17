from regex_validator import find_postal_codes
from data_parser import get_text_from_input, get_text_from_file, get_text_from_url


def main():
    while True:
        print("\n=== Поиск почтовых индексов РФ ===")
        print("1. Ввести текст вручную")
        print("2. Найти индексы в файле")
        print("3. Найти индексы на веб-странице (по URL)")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ")

        text_to_search = ""

        if choice == '1':
            text_to_search = get_text_from_input()
        elif choice == '2':
            filepath = input("Введите путь к файлу (например, data.txt): ")
            text_to_search = get_text_from_file(filepath)
        elif choice == '3':
            url = input("Введите URL (например, https://example.com): ")
            text_to_search = get_text_from_url(url)
        elif choice == '4':
            print("Завершение программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")
            continue

        if text_to_search:
            found_codes = find_postal_codes(text_to_search)
            if found_codes:
                print(f"\n✅ Найдены индексы ({len(found_codes)} шт.):")
                for idx, code in enumerate(found_codes, 1):
                    print(f"  {idx}. {code}")
            else:
                print("\n❌ Почтовые индексы в тексте не найдены.")


if __name__ == "__main__":
    main()