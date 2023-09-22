from random import randint
from math import gcd


MIN_VALUE, MAX_VALUE = 1, 100
ROUNDS = 3
TASK = 'Find the greatest common divisor of given numbers.'


def generate_gcd():

    num1 = randint(MIN_VALUE, MAX_VALUE)
    num2 = randint(MIN_VALUE, MAX_VALUE)
    correct_answer = str(gcd(num1, num2))

    return correct_answer, num1, num2


def get_questions_and_answers():

    questions_list = []
    correct_answers_list = []

    for i in range(ROUNDS):
        correct_answer, num1, num2 = generate_gcd()
        questions_list.append(f'{num1} {num2}')
        correct_answers_list.append(correct_answer)

    return questions_list, correct_answers_list
