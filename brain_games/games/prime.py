from random import randint
from math import sqrt


MIN_VALUE, MAX_VALUE = 2, 100
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def generate_prime():

    num = randint(MIN_VALUE, MAX_VALUE)
    question = num
    correct_answer = 'yes' if is_prime(num) else 'no'

    return question, correct_answer
