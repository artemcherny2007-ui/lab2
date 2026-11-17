import requests
import os


def get_text_from_input() -> str:
    """Получает текст от пользователя через стандартный ввод консоли."""
    print("Введите текст для поиска индексов (нажмите Enter для завершения):")
    return input("> ")


def get_text_from_file(filepath: str) -> str:
    """Читает текст из локального файла с обработкой ошибок."""
    if not os.path.exists(filepath):
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return ""

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return ""


def get_text_from_url(url: str) -> str:
    """Скачивает HTML-код веб-страницы по указанному URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return ""