# для прерывания потока ввода используется Ctrl+D
def main():
    import sys
    input_data = sys.stdin.read

    # парсим входные данные
    data = input_data().strip().split('\n')

    # кол-во строк
    n = int(data[0])

    # логика разбиения для каждой строки
    for i in range(1, n + 1):
        booking = data[i].split(',')
        book_ref = booking[0]
        book_date = booking[1]
        total_amount = booking[2]

        # делим по рублям и копейкам
        rub, kop = total_amount.split('.')

        # форматируем вывод
        print(f'Номер бронирования {book_ref}, забронирован {book_date}. Цена: {rub} руб. {kop} коп.')


if __name__ == "__main__":
    main()
