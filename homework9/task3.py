from collections import Counter

with open('D:\\homework9\\task3_input.txt', 'r', encoding='utf-8') as input_file, \
     open('D:\\homework9\\task3_output.txt', 'w', encoding='utf-8') as output_file:

    for line in input_file:
        words = line.strip().split()
        if words:
            freq = Counter(words)
            most_common_word, count = freq.most_common(1)[0]
            output_line = f"{most_common_word} {count}"
            output_file.write(output_line + '\n')
            
            print(output_line)


