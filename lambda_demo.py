from functools import reduce


def demo_simple_lambda():
    lambda_function = lambda x: x * 10
    print(f'Lambda function to multiply input by 10\n'
          f'{lambda_function(10)}')

    f = lambda x, y, z: x + y + z
    print(f'Lambda function that adds the three input numbers\n'
          f'{f(5, 6, 2)}\n')


def demo_lambda_functions():
    print(f'Multiply each element in a list with 10\n'
          f'{list(map(lambda x: x*10, [1, 2, 3, 4, 5]))}\n')

    ages = list(range(1, 101))
    print(f'Given people with ages\n'
          f'{ages}\n')
    print(f'Filter out ages who are allowed to watch R-rated movies.\n'
          f'{list(filter(lambda age: age>=18, ages))}\n')
    print(f'I expect the list below to be the same.\n'
          f'{[age for age in ages if age >= 18]}\n')


# [1,2,3,4,5]   f(x,y)  = x+y
# [1,2,3,4,5]   f(1,2)  = 1+2  = 3
# [  3,3,4,5]   f(3,3)  = 3+3  = 6
# [    6,4,5]   f(6,4)  = 6+4  = 10
# [     10,5]   f(10,5) = 10+5 = 15
# 15
def demo_reduce():
    input_range = list(range(1, 5+1))
    print(f'Given this list of input numbers\n'
          f'{input_range}\n')
    print(f'The sum of all the numbers in the list is\n'
          f'{reduce(lambda x, y: x+y, input_range)}')


if __name__ == '__main__':
    choice = input('Enter your demo choice:\n'
                   '1: Demo Simple Lambda\n'
                   '2: Demo Map & Filter\n'
                   '3: Demo Reduce\n'
                   'Enter your choice number:\t')
    print('\n')
    if 1 == int(choice):
        demo_simple_lambda()
    elif 2 == int(choice):
        demo_lambda_functions()
    elif 3 == int(choice):
        demo_reduce()
    else:
        print('INVALID CHOICE. Please input only numbers 1-3.')
