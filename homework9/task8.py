import json
import csv


JSON_FILE = 'D:\\homework9\\employees.json'
CSV_FILE = 'D:\\homework9\\employees.csv'

def load_json():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def json_to_csv():
    data = load_json()
    headers = list(data[0].keys())
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for emp in data:
            row = emp.copy()
            row['languages'] = ','.join(row['languages'])
            row['car'] = str(row['car'])
            writer.writerow(row)

def add_employee_json():
    data = load_json()
    name = input('Имя Фамилия: ')
    birthday = input('Дата рождения (дд.мм.гггг): ')
    height = int(input('Рост см: '))
    weight = float(input('Вес кг: '))
    car_input = input('Есть машина? Введите 1 (да) или 0 (нет): ')
    car = car_input == '1'
    languages = input('Языки программирования через запятую: ').split(',')
    languages = [lang.strip() for lang in languages if lang.strip()]
    new_emp = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages
    }
    data.append(new_emp)
    save_json(data)
    print('Сотрудник добавлен в JSON.')

def add_employee_csv():
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        name = input('Имя Фамилия: ')
        birthday = input('Дата рождения (дд.мм.гггг): ')
        height = input('Рост см: ')
        weight = input('Вес кг: ')
        car_input = input('Есть машина? Введите 1 (да) или 0 (нет): ')
        car = car_input == '1'
        languages = input('Языки программирования через запятую: ')
        writer.writerow([name, birthday, height, weight, str(car), languages])
        print('Сотрудник добавлен в CSV.')

def search_employee_by_name():
    name = input('Введите имя для поиска: ').lower()
    data = load_json()
    found = False
    for emp in data:
        if name in emp['name'].lower():
            print(emp)
            found = True
    if not found:
        print('Сотрудник не найден.')

def filter_by_language():
    lang = input('Введите язык программирования: ').lower()
    data = load_json()
    filtered = [emp for emp in data if any(l.lower() == lang for l in emp['languages'])]
    if filtered:
        for emp in filtered:
            print(emp)
    else:
        print('Сотрудников с таким языком нет.')

def filter_by_birth_year():
    year = int(input('Введите год рождения для фильтра (<): '))
    data = load_json()
    heights = []
    for emp in data:
        birth_year = int(emp['birthday'].split('.')[-1])
        if birth_year < year:
            heights.append(emp['height'])
    if heights:
        print('Средний рост:', sum(heights) / len(heights))
    else:
        print('Сотрудников с годом рождения меньше заданного нет.')

def main_menu():
    while True:
        print('''Выберите действие:
1 - Конвертация JSON в CSV
2 - Добавить сотрудника в JSON
3 - Добавить сотрудника в CSV
4 - Поиск сотрудника по имени
5 - Фильтр по языку программирования
6 - Фильтр по году рождения
0 - Выход''')
        choice = input('Ваш выбор: ')
        match choice:
            case '1':
                json_to_csv()
                print('JSON сконвертирован в CSV.')
            case '2':
                add_employee_json()
            case '3':
                add_employee_csv()
            case '4':
                search_employee_by_name()
            case '5':
                filter_by_language()
            case '6':
                filter_by_birth_year()
            case '0':
                print('Выход.')
                break
            case _:
                print('Неверный выбор. Попробуйте снова.')

if __name__ == '__main__':
    main_menu()
