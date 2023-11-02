def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить программу', sep='\n')
    choice = int(input())
    return choice

def print_result(phone_book):
    for record in phone_book:
        print(f'{record["Фамилия"]}, {record["Имя"]}, {record["Телефон"]}, {record["Описание"]}')

def find_by_lastname(phone_book, last_name):
    found_records = []
    for record in phone_book:
        if record["Фамилия"] == last_name:
            found_records.append(record)
    if found_records:
        return found_records
    else:
        return "Запись не найдена"

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record["Фамилия"] == last_name:
            record["Телефон"] = new_number
            return "Номер телефона успешно изменен"
    return "Запись не найдена"

def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record["Фамилия"] == last_name:
            phone_book.remove(record)
            return "Запись успешно удалена"
    return "Запись не найдена"

def find_by_number(phone_book, number):
    found_records = []
    for record in phone_book:
        if record["Телефон"] == number:
            found_records.append(record)
    if found_records:
        return found_records
    else:
        return "Запись не найдена"

def add_user(phone_book, user_data):
    fields = user_data.split(',')
    if len(fields) == 4:
        record = {
            "Фамилия": fields[0].strip(),
            "Имя": fields[1].strip(),
            "Телефон": fields[2].strip(),
            "Описание": fields[3].strip()
        }
        phone_book.append(record)
        return "Запись успешно добавлена"
    else:
        return "Ошибка при добавлении записи. Правильный формат: Фамилия, Имя, Телефон, Описание"

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('lastname ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ')
            result = add_user(phone_book, user_data)
            print(result)
            if result == "Запись успешно добавлена":
                write_txt('phonebook.txt', phone_book)
        choice = show_menu()

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            values = line.strip().split(',')
            if len(values) == 4:
                record = dict(zip(fields, values))
                phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            values = [record[field] for field in ['Фамилия', 'Имя', 'Телефон', 'Описание']]
            phout.write(','.join(values) + '\n')

work_with_phonebook()
