import os
import sys
import time


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_hacker_style(text, color_code="\033[92m"):  # По умолчанию зеленый
    print(f"{color_code}{text}\033[0m")  # Цветной текст
    time.sleep(0.1)  # Задержка для эффекта


def mysterious_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char == '\n':  # Если символ — новая строка, не шифруем его
            encrypted_text += char
        else:
            encrypted_char = chr((ord(char) + shift) % 256)  # Сдвиг вправо
            encrypted_text += encrypted_char
    return encrypted_text


def mysterious_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char == '\n':  # Если символ — новая строка, не шифруем его
            decrypted_text += char
        else:
            decrypted_char = chr((ord(char) - shift) % 256)  # Сдвиг влево
            decrypted_text += decrypted_char
    return decrypted_text


def print_with_delay(text, speed):
    for char in text:
        print(char, end='', flush=True)  # Печать символа без перехода на новую строку
        time.sleep(60 / speed)  # Задержка для эффекта
    print()  # Переход на новую строку после завершения печати


def main():
    clear_console()
    print_hacker_style("=== Мистическая Шифровка ===")
    print("=" * 40)  # Разделитель

    choice = input("Выберите действие:\n0 - Зашифровать текст\n1 - Расшифровать текст\nВаш выбор: ")

    if choice not in ['0', '1']:
        print_hacker_style("Неверный выбор. Завершение...", "\033[91m")  # Красный цвет для ошибки
        sys.exit(1)

    print_hacker_style("Введите текст (для завершения ввода введите 'END'):")
    print("=" * 40)  # Разделитель

    # Считывание многострочного текста
    text = ""
    while True:
        line = input()
        if line == 'END':
            break
        text += line + '\n'  # Добавляем новую строку к тексту

    while True:
        try:
            shift = int(input("Введите количество сдвигов: "))
            break  # Выход из цикла, если ввод корректный
        except ValueError:
            print_hacker_style("Ошибка: пожалуйста, введите целое число для сдвига.",
                               "\033[91m")  # Красный цвет для ошибки

    print("=" * 40)  # Разделитель

    if choice == '0':
        encrypted_text = mysterious_encrypt(text, shift)
        print_hacker_style("Зашифрованный текст:", "\033[92m")  # Зеленый цвет для зашифрованного текста
        print_with_delay(encrypted_text, 1200)  # Печать текста со скоростью 1200 символов в минуту
    else:
        decrypted_text = mysterious_decrypt(text, shift)
        print_hacker_style("Расшифрованный текст:", "\033[92m")  # Зеленый цвет для расшифрованного текста
        print_with_delay(decrypted_text, 1200)  # Печать текста со скоростью 1200 символов в минуту

    print("=" * 40)  # Разделитель
    print_hacker_style("Завершение программы...")


if __name__ == "__main__":
    main()
