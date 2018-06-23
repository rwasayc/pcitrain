import time

people = [
    ('Seymour', 'BOS'),
    ('Franny', 'DAL'),
    ('Zooey', 'CAK'),
    ('Walt', 'MIA'),
    ('Buddy', 'ORD'),
    ('Les', 'OMA')
]

flights = {}
for line in open('schedule.txt'):
    origin, dest, depart, arrive, price = line.strip().split(',')
    flights.setdefault((origin, dest), [])

    flights[(origin, dest)].append((depart, arrive, int(price)))


def get_minutes(t):
    x = time.strptime(t, '%H:%M')
    return x[3] * 60 + x[4]


