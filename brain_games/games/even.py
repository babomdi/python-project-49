from brain_games.engine import eng
from brain_games.functions import random_even


def even_logic():

    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    question_lst = list()
    correct_ans_lst = list()

    for i in range(3):
        correct_ans, num = random_even()
        question_lst.append(num)
        correct_ans_lst.append(correct_ans)

    eng(task, question_lst, correct_ans_lst)
