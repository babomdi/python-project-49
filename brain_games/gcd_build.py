def gcd():

    import random
    import math

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_ans = str(math.gcd(num1, num2))

    return correct_ans, num1, num2
