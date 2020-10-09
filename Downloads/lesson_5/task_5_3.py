#Ok
with open('user_text.txt', 'r') as file:
    sum = 0
    lines = file.readlines()
    for i, line in enumerate(lines):
        words = line.split()
        salary = int(words[1])
        if salary < 20000:
            print(f'Зарплату меньше 20 тысяч получает {words[0]}')
        sum = sum + salary
        num = i + 1

print(f'Средняя зарплата сотрудников: {sum / num}')
