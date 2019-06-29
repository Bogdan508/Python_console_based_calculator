from colorama import init
import time
from colorama import Fore, Back, Style
init()

def first_op():
    try:
        print(Back.CYAN)
        a = input('Enter the first number: ')
        float(a)

        test = int(0)
        global first_v
        first_v = int(0)
        if float(a) == float(test):
            first_v = 0
        else:
            first_v = a
        float(first_v)
    except:
        print(Back.RED)
        print('Not a number')
        print('Select a num type value')
        time.sleep(0.5)
        first_op()

def oper_c():
    print(Back.CYAN)
    global symb
    print(first_v, ' ?', ' ?')
    symb = input('Choose the operator(+, -, *, /, %(Modulus), %of(percent of) and **): ')
    if symb == '+' or symb == '-' or symb == '*' or symb == '/' or symb == '%' or symb == '%of' or symb == '**':
        oper = True
    else:
        print(Back.RED)
        print('Wrong operator')
        oper = False
    if oper is False:
        print('Select the correct operator')
        time.sleep(0.5)
        oper_c()

def sec_op():
        try:
            print(Back.CYAN)
            print(first_v,'', symb, ' ?')
            b = input('Enter the second number : ')
            float(b)

            test = int(0)
            global second_v
            second_v = int(0)
            if float(b) == float(test):
                second_v = 0
            else:
                second_v = b
            float(first_v)
        except:
            print(Back.RED)
            print('Not a number')
            print('Press Enter to select a number')
            time.sleep(0.5)
            sec_op()

def calculation():
    first_op()
    oper_c()
    sec_op()
    global res
    if symb == '+':
        res = float(first_v) + float(second_v)
        result()
    elif symb == '-':
        res = float(first_v) - float(second_v)
        result()
    elif symb == '*':
        res = float(first_v) * float(second_v)
        result()
    elif symb == '/':
        if second_v == 0:
            print(Back.RED)
            res = 'cannot be divided by zero'
            print(first_v,'', symb,'', second_v)
            print(res)
        else:
            print(Back.CYAN)
            res = float(first_v) / float(second_v)
            result()
    elif symb == '%':
        res = float(first_v) % float(second_v)
        result()
    elif symb == '%of':
        res = (float(first_v) * float(second_v))/100
        result()
    elif symb == '**':
        if float(first_v) == 0 and float(second_v) == 0:
            res = 0
            result()
        else:
            try:
                res = float(first_v) ** float(second_v)
                result()
            except:
                print(Back.RED)
                print('Result is too large')
                print('Please choose another value')
                time.sleep(0.5)
                more_operations()

def result():
    print(Back.GREEN)
    print(first_v,'', symb,'', second_v)
    print('The answer is: ', res)

def more_operations():
    print(Back.CYAN)
    moreop = input('One more operation?(y/n(Enter)): ')
    while moreop == 'y':
        calculation()
        print(Back.CYAN)
        moreop = input('One more operation?(y/n(Enter)): ')
    if moreop == 'n' or moreop == '':
        print(Back.CYAN)
        print('Closing...')
        time.sleep(0.5)
        quit()
    else:
        exit()

def exit():
    print(Back.RED)
    x = input('Type y(yes)/n(no) or press Enter(no): ')
    if x == 'y':
        calculation()
        more_operations()
    elif x == 'n' or x == '':
        print(Back.CYAN)
        print('Closing...')
        time.sleep(0.5)
        quit()
    else:
        sectry()

def sectry():
    print(Back.RED)
    y = input('Type y(yes)/n(no) or press Enter(no): ')
    if y == 'y':
        calculation()
        more_operations()
    elif y == 'n' or y == '':
        print(Back.CYAN)
        print('Closing...')
        time.sleep(0.5)
        quit()
    else:
        sectry()

calculation()
more_operations()
