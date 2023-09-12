from brain_games.engine import eng
from brain_games.functions import random_prime
from random import randint


def prime_logic():

    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions_lst = list()
    correct_ans_lst = list()

    for i in range(3):
        num = randint(1, 100)
        correct_ans = random_prime(num)
        questions_lst.append(num)
        correct_ans_lst.append(correct_ans)

    eng(task, questions_lst, correct_ans_lst)
