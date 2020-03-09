import random
from string import digits


def idv3(size=13, chars=digits):
    return int(''.join(random.choice(chars) for _ in range(size)))


def idv1(size=10, chars=digits):
    return int(''.join(random.choice(chars) for _ in range(size)))
