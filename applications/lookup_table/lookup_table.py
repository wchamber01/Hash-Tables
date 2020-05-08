import math
import random


def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    # v = math.pow(x, y)
    # v = math.factorial(v)
    # v //= (x+y)
    # v %= 982451653
    # return v

    cache = {}

    def factorial(x, y):
        if (x, y) not in cache:
            v = math.pow(x, y)
            v = math.factorial(v)
            v //= (x+y)
            v %= 982451653
            cache[str(x+y)] = v
            print(cache[str(x+y)])
        return str(cache[str(x+y)])
    return factorial


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
