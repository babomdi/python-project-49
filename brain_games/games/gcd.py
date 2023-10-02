from random import randint
from math import gcd


MIN_VALUE, MAX_VALUE = 1, 100
TASK = 'Find the greatest common divisor of given numbers.'


def generate_gcd():

    num1 = randint(MIN_VALUE, MAX_VALUE)
    num2 = randint(MIN_VALUE, MAX_VALUE)
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))

    return question, correct_answer
