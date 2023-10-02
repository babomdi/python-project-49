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

    if is_even(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
