with open('D:\\homework9\\students.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) < 3:
            continue
        try:
            score = int(parts[2])
        except ValueError:
            continue
        if score < 3:
            print(f"{parts[0]} {parts[1]} с оценкой {score}")
