# циклічний зсув
n = 1
# алфавіт
abc = 'abcdefghijklmnopqrstuvwxyz'

# функція для шифрування рядка
def encrypt_string(input_string, abc, cipher):
    # перевіряємо чи довжина алфавіту відповідає довжині ключа
    if len(cipher) != len(abc):
        raise ValueError("Не допустима довжина перестановки!")
    # Формуємо словник
    cipher_dict = {abc[i]: cipher[i] for i in range(len(abc))}
    # приводимо строку до нижнього регістру і замінюємо букви значеннями із словника під відповідним ключем
    # якщо ключ не зустрічаєтьс повертаємо той самий символ
    encrypted_str = ''.join(cipher_dict.get(char, char) for char in input_string.lower())
    return encrypted_str

# зчитуємо рядок з файлу
with open('input.txt', 'r', encoding='utf-8') as file:
    input_string = file.read()

with open('cipher.txt', 'r', encoding='utf-8') as file:
    cipher = file.read()    

# виконуємо шифрування та виводимо результат
encrypted_output = encrypt_string(input_string, abc, cipher)
output = "Зашифровані: " + encrypted_output + "\n"

# записуємо результат у файл
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(output)

# проводимо розшифрування
decrypted_output = encrypt_string(encrypted_output, cipher, abc)
output += "Дешифровані: " + decrypted_output + "\n"

# доповнюємо вихідний файл розшифрованим текстом
with open('output.txt', 'a', encoding='utf-8') as file:
    file.write(output)

print(output)
