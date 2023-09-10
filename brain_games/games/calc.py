def calc_logic():

    import random
    from brain_games.engine import eng

    task = 'What is the result of the expression?'
    questions_lst = []
    correct_ans_lst = []
    operators = ['+', '-', '*']

    for i in range(3):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        oper = random.choice(operators)
        questions_lst.append(f'{num1} {oper} {num2}')

        if oper == '+':
            correct_ans = num1 + num2
        elif oper == '-':
            correct_ans = num1 - num2
        else:
            correct_ans = num1 * num2
        correct_ans = str(correct_ans)

        correct_ans_lst.append(correct_ans)

    eng(task, questions_lst, correct_ans_lst)
