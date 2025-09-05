import re

with open('D:\\homework9\\stop_words.txt', 'r', encoding='utf-8') as f:
    stop_words = f.read().strip().split()

pattern = re.compile('|'.join(map(re.escape, stop_words)), flags=re.IGNORECASE)

file_name = input("Введите имя текстового файла: ")

with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        def replacer(match):
            return '*' * len(match.group())
        censored_line = pattern.sub(replacer, line)
        print(censored_line, end='')
