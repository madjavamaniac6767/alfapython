# для прерывания потока ввода используется Ctrl+D
def main():
    import sys
    input_data = sys.stdin.read

    # Разбиваем входные данные
    data = input_data().strip().split('\n')

    # Количество билетов
    num = int(data[0])

    # Создаем сет для уникальных значений ticket_no, flight_id
    seen = set()

    output = []

    # Логика для каждого билета
    for i in range(1, num + 1):
        ticket_info = data[i].split(',')
        ticket_no = ticket_info[0]
        flight_id = ticket_info[1]

        # Проверка на уникальность
        if (ticket_no, flight_id) not in seen:
            seen.add((ticket_no, flight_id))
            output.append(data[i])

    # Выводим каждую строку
    for line in output:
        print(line)


if __name__ == "__main__":
    main()
