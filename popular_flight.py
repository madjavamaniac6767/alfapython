from collections import defaultdict


def find_popular_flight(input_data):
    flight_count = defaultdict(int)

    # первая строчка нам не нужна
    for line in input_data[1:]:
        parts_data = line.split(',')
        if len(parts_data) != 4:
            continue
        _, flight_id, _, _ = line.split(',')
        flight_count[int(flight_id)] += 1

    max_count = max(flight_count.values())

    most_popular_flights = [str(flight_id) for flight_id, count in flight_count.items() if count == max_count]

    # сортируем в естественном порядке
    most_popular_flights.sort()

    res_string = ', '.join(most_popular_flights)

    return res_string


def result():
    data = ['5',
            'EXGJGJ521,3,252st,10;C',
            '2Jw2n5l,3,252st,16;F',
            'KUIK2YL,1,Номер:327ggs,30;A',
            '8XSOVGVNDQ,1,Номер:327ggs,51;A',
            'DRXGH62d,5,7733d,62;A']

    return find_popular_flight(data)


print(result())
