def calc_logic():

    from brain_games.engine import eng
    from brain_games.functions import random_calc

    task = 'What is the result of the expression?'
    questions_lst = []
    correct_ans_lst = []

    for i in range(3):
        correct_ans, num1, num2, oper = random_calc()
        questions_lst.append(f'{num1} {oper} {num2}')
        correct_ans_lst.append(str(correct_ans))

    eng(task, questions_lst, correct_ans_lst)
