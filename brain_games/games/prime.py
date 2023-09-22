from random import randint
from math import sqrt


MIN_VALUE, MAX_VALUE = 2, 100
ROUNDS = 3
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

    return correct_answer


def generate_prime():

    num = randint(MIN_VALUE, MAX_VALUE)

    correct_answer = is_prime(num)

    return correct_answer, num


def get_questions_and_answers():

    questions_list = []
    correct_answers_list = []

    for i in range(ROUNDS):
        correct_answer, num = generate_prime()
        questions_list.append(num)
        correct_answers_list.append(correct_answer)

    return questions_list, correct_answers_list
