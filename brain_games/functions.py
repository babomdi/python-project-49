def random_even():

    from random import randint

    num = randint(0, 100)

    if num % 2 == 0:
        correct_ans = 'yes'
    else:
        correct_ans = 'no'

    return correct_ans, num


def random_calc():

    from random import randint, choice

    operators = ['+', '-', '*']
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    random_oper = choice(operators)

    if random_oper == '+':
        correct_ans = num1 + num2
    elif random_oper == '-':
        correct_ans = num1 - num2
    else:
        correct_ans = str(num1 * num2)

    return correct_ans, num1, num2, random_oper


def random_gcd():

    from random import randint
    from math import gcd

    num1 = randint(1, 100)
    num2 = randint(1, 100)
    correct_ans = str(gcd(num1, num2))

    return correct_ans, num1, num2


def random_progression():

    from random import randint

    prog = []
    num = randint(1, 10)
    prog.append(num)
    diff = randint(1, 20)

    for i in range(9):
        next_num = num + diff
        prog.append(next_num)
        num = next_num

    hidden_elem = randint(0, 9)
    correct_ans = str(prog[hidden_elem])
    prog[hidden_elem] = '..'

    return correct_ans, prog


def random_prime():

    from random import randint

    num = randint(1, 100)
    
    if num > 1:
        for i in range(1, num):
            if i > 1 and num % i == 0:
                correct_ans = 'no'
                break
            else:
                correct_ans = 'yes'
    else:
        correct_ans = 'no'

    return correct_ans, num
