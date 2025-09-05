def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

with open('D:\\homework9\\task7_input.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file, start=1):
        shifted_line = caesar_cipher(line.rstrip('\n'), i)
        print(shifted_line)
