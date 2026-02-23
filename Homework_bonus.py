import random

# setting up choosing randomly numbers
def _random_numbers_ ():
    random_number = random.randint (1,10)
    random_number_2 = random.randint (1,10)
    return random_number,random_number_2

num_1, num_2 = _random_numbers_()

def _random_math_operation ():
    random_math_operation = random.choice ('+' '-' '*' '/')
    return random_math_operation

math_operation = _random_math_operation()

def _oper_ (random_number,random_number_2,random_math_operation):
    if random_math_operation == '+':
        correct_answer = random_number + random_number_2
        return correct_answer
    elif random_math_operation == '-':
        correct_answer = random_number - random_number_2
        return correct_answer
    elif random_math_operation == '*':
        correct_answer = random_number * random_number_2
        return correct_answer
    elif random_math_operation == '/':
        correct_answer = random_number / random_number_2
        return correct_answer
oper = _oper_(num_1,num_2,math_operation)

def basic_math (num_1, math_operation, num_2, oper):
    question = (f'{num_1} {math_operation} {num_2} = ?')
    print (question)
    answer = float (input('enter your answer: '))
    _oper = int (oper*10) / 10
    if round (answer,1) == round (oper,1):
        print ('Correct!')
    else:
        print (f'Wrong... the answer was {_oper}')

_random_numbers_()
_oper_ (_random_numbers_,_oper_,_random_math_operation)
basic_math (num_1, math_operation, num_2, oper)