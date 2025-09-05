import re

total = 0
with open('D:\\homework9\\task6_input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        numbers = re.findall(r'\d+', line)  
        total += sum(int(number) for number in numbers)  
print(total)
