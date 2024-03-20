def process_text(text, gamma, operation='encrypt'):
    processed_text = ""
    for i in range(len(text)):
        char = text[i]
        gamma_char = gamma[i % len(gamma)]
        if char.isalpha():
            shift = ord(gamma_char) - ord('a')
            if operation == 'encrypt':
                processed_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif operation == 'decrypt':
                processed_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            processed_char = char
        processed_text += processed_char
    return processed_text

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

input_file_path = "input.txt"
output_file_path = "output.txt"
gamma = "iwqoidjwqojdlw"

plain_text = read_file(input_file_path).lower()

encrypted_text = process_text(plain_text, gamma, operation='encrypt')
print("Encrypted:", encrypted_text)

write_file(output_file_path, encrypted_text)

decrypted_text = process_text(encrypted_text, gamma, operation='decrypt')
print("Decrypted:", decrypted_text)

write_file(output_file_path, decrypted_text)
