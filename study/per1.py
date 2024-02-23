import random

def is_happen(*rates: list[float]) -> bool:
    for r in rates:
        if random.random() > r:
            return False
    return True

def run():
    rate1 = 0.02
    rate2 = 0.5
    days = 1000
    counter = []

    for i in range(days):
        c = 1
        # while (random.random() > rate1) or (random.random() > rate2):
        while (not is_happen(rate1, rate2)):
            c += 1
        counter.append(c)

    counter.sort(key=lambda x:x, reverse=True)
    print(counter)
    print([x for x in counter if x > 100])
    print(len([x for x in counter if x > 100]))
    print(len([x for x in counter if x == 1]))


if __name__ == '__main__':
    run()