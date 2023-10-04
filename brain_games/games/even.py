from random import randint


MIN_VALUE, MAX_VALUE = 0, 100
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):

    if num % 2 == 0:
        return True

    return False


def generate_even():

    num = randint(MIN_VALUE, MAX_VALUE)
    question = num

    correct_answer = 'yes' if is_even(num) else 'no'

    return question, correct_answer
