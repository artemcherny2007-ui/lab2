import unittest
from regex_validator import find_postal_codes


class TestPostalCodeRegex(unittest.TestCase):

    def test_valid_standard_codes(self):
        """Проверка стандартных корректных 6-значных индексов."""
        text = "Мой индекс 123456, а у друга 999999."
        result = find_postal_codes(text)
        self.assertEqual(result, ['123456', '999999'])

    def test_valid_ru_prefix(self):
        """Проверка индексов с префиксом страны RU-."""
        text = "Отправка в RU-101000 и RU-450000."
        result = find_postal_codes(text)
        self.assertEqual(result, ['RU-101000', 'RU-450000'])

    def test_invalid_starts_with_zero(self):
        """Российский индекс не может начинаться с нуля."""
        text = "Неправильные индексы: 012345 и 099999."
        result = find_postal_codes(text)
        self.assertEqual(result, [])

    def test_invalid_length(self):
        """Проверка отсечения индексов неверной длины (5 или 7 цифр)."""
        text = "Слишком короткий 12345 и длинный 1234567."
        result = find_postal_codes(text)
        self.assertEqual(result, [])

    def test_inside_words_or_numbers(self):
        """Проверка, что регулярка не захватывает индексы внутри других слов или больших чисел."""
        text = "Номер телефона 89991234567, товар ID123456, сумма 123456руб."
        result = find_postal_codes(text)
        self.assertEqual(result, [])

    def test_empty_string(self):
        """Проверка поведения при пустой строке."""
        result = find_postal_codes("")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()