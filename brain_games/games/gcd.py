def gcd_logic():

    from brain_games.engine import eng
    from brain_games.functions import random_gcd

    task = 'Find the greatest common divisor of given numbers.'
    questions_lst = []
    correct_ans_lst = []

    for i in range(3):
        correct_ans, num1, num2 = random_gcd()
        questions_lst.append(f'{num1} {num2}')
        correct_ans_lst.append(correct_ans)

    eng(task, questions_lst, correct_ans_lst)
