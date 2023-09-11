def calc():

    import random

    operators = ['+', '-', '*']
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    oper = random.choice(operators)

    if oper == '+':
        correct_ans = num1 + num2
    elif oper == '-':
        correct_ans = num1 - num2
    else:
        correct_ans = num1 * num2

    return str(correct_ans), num1, num2, oper
