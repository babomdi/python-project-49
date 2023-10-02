from brain_games.cli import welcome_user
import prompt


ROUNDS = 3


def run_game(task, get_question_and_answer):

    name = welcome_user()
    print(task)

    for i in range(ROUNDS):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Answer: ')
        correct_answer = correct_answer

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        elif answer == correct_answer and i < 2:
            print('Correct!')
        else:
            print('Correct!')
            print(f'Congratulations, {name}!')
