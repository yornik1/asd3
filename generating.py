import random


def generate_file(n, filename='data.in'):
    l = list(range(0, n))
    random.shuffle(l)
    with open(filename, 'w') as f:
        for i in l:
            f.write(str(i) + '\n')
            # f.write(str(random.randint(0, 18446744073709551616))+'\n')


generate_file(1000000)
