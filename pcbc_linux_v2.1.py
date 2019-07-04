import time
import os
import sys
from colorama import Back, Style

upper_sym = '-'
sq_root = '\u221a'

def cmd_clean():
    print(Style.RESET_ALL)
    os.system('clear')
    print(Style.RESET_ALL)

def first_op():
    print(Style.RESET_ALL, end = '')
    print('    ','-------------')
    print('    ','| ', end = '')
    print(Back.CYAN, end = '')
    print(' ?',' ?',' ? ', end = '')
    print(Style.RESET_ALL, end = '')
    print(' |')
    print('    ','-------------')
    try:
        print(Back.CYAN)
        a = input('Enter the first number: ')
        cmd_clean()
        float(a)

        test = int(0)
        global first_v
        first_v = int(0)
        if float(a) == float(test):
            first_v = 0
        else:
            first_v = a
        float(first_v)

        global first_len
        if first_v == 0:
            first_len = 1
        else:
            first_len = len(first_v)
        global first_up_line
        global first_down_line
        global zero_down_line
        first_up_line = first_len * '-'
        first_down_line = first_len * upper_sym
        zero_down_line = 12 * upper_sym
    except:
        cmd_clean()
        print(Back.RED, end = '')
        print(a, 'is not a number')
        print('Select a num type value')
        print('')
        time.sleep(0.5)
        first_op()

def oper_c():
    global symb
    print(Style.RESET_ALL, end = '')
    print('    ','---' + first_up_line + '---------')
    print('    ','| ', end = '')
    print(Back.CYAN, end = '')
    sfirst_v = str(first_v)
    print('', sfirst_v, ' ?', ' ? ', end = '')
    print(Style.RESET_ALL, end = '')
    print(' |')
    print('    ',first_down_line + zero_down_line)
    print(Back.CYAN)
    print('   |  +  |  -  |  *  |  /  |  ')
    print('   |  %  | %of |  ** | sqr |  ')
    print('')
    print('(% - Modulus, ** - Exponent         ')
    print('%of - Percentage, sqr - square root)')
    print('')
    symb = input('Choose the operator: ')
    cmd_clean()
    if symb == '+' or symb == '-' or symb == '*' or symb == '/' or symb == '%' or symb == '%of' or symb == '**' or symb == 'sqr':
        oper = True
        if symb == 'sqr':
            res = float(first_v) ** 0.5
            print(Style.RESET_ALL, end = '')
            print('    ','-----------' + first_up_line)
            print('    ','| ', end = '')
            print(Back.CYAN, end = '')
            sfirst_v = str(first_v)
            print('',sq_root, 'of', sfirst_v,'', end = '')
            print(Style.RESET_ALL, end = '')
            print(' |')
            print('    ',first_down_line + '-----------')
            print(Back.GREEN)
            print('The answer is: ', res)
            print('')
            more_operations()

        global oper_len
        oper_len = len(symb)
        global sec_up_line
        global sec_down_line
        global add1_down
        sec_up_line = oper_len * '-'
        sec_down_line = oper_len * upper_sym
        add1_down = 11 * upper_sym
    else:
        print(Back.RED, end = '')
        print('        Wrong operator        ')
        oper = False
    if oper is False:
        print(' Select the correct operator  ')
        print('')
        time.sleep(0.5)
        oper_c()

def sec_op():
    try:
        print(Style.RESET_ALL, end = '')
        print('    ','--' + first_up_line + sec_up_line + '---------')
        print('    ','| ', end = '')
        print(Back.CYAN, end = '')
        sfirst_v = str(first_v)
        print('', sfirst_v,'', symb, ' ? ', end = '')
        print(Style.RESET_ALL, end = '')
        print(' |')
        print('    ',first_down_line + sec_down_line + add1_down)

        print(Back.CYAN)
        b = input('Enter the second number : ')
        cmd_clean()
        float(b)

        test = int(0)
        global second_v
        second_v = int(0)
        if float(b) == float(test):
            second_v = 0
        else:
            second_v = b
        float(first_v)

        global sec_len
        if second_v == 0:
            sec_len = 1
        else:
            sec_len = len(second_v)
        global third_up_line
        global third_down_line
        global add2_down
        third_up_line = sec_len * '-'
        third_down_line = sec_len * upper_sym
        add2_down = 10 * upper_sym
    except:
        cmd_clean()
        print(Back.RED, end = '')
        print(b, 'is not a number')
        print('Select a num type value')
        print('')
        time.sleep(0.5)
        sec_op()

def calculation():
    cmd_clean()
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
            print(Style.RESET_ALL, end = '')
            print('    ','--' + first_up_line + sec_up_line + third_up_line + '--------')
            print('    ','| ', end = '')
            print(Back.CYAN, end = '')
            sfirst_v = str(first_v)
            ssecond_v = str(second_v)
            print('', sfirst_v,'', symb,'', ssecond_v,'', end = '')
            print(Style.RESET_ALL, end = '')
            print(' |')
            print('    ',first_down_line + sec_down_line + third_down_line + add2_down)
            print(Back.RED, end = '')
            res = 'Cannot be divided by zero'
            print('')
            print(res)
            print('')
            more_operations()
        else:
            print(Back.CYAN, end = '')
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
                print('    Result is too large    ')
                print('Please choose another value')
                print('')                
                time.sleep(0.5)
                more_operations()

def result():
    print(Style.RESET_ALL, end = '')
    print('    ','--' + first_up_line + sec_up_line + third_up_line + '--------')
    print('    ','| ', end = '')
    print(Back.CYAN, end = '')
    sfirst_v = str(first_v)
    ssecond_v = str(second_v)
    print('', sfirst_v,'', symb,'', ssecond_v,'', end = '')
    print(Style.RESET_ALL, end = '')
    print(' |')
    print('    ',first_down_line + sec_down_line + third_down_line + add2_down)
    print(Back.GREEN)
    print('The answer is: ', res)
    print('')

def more_operations():
    print(Back.CYAN, end = '')
    moreop = input('One more operation?(y/n(Enter)): ')
    cmd_clean()
    while moreop == 'y' or moreop =='Y':
        calculation()
        print(Back.CYAN, end = '')
        moreop = input('One more operation?(y/n(Enter)): ')
    if moreop == 'n' or moreop == 'N' or moreop == '':
        print(Back.CYAN)
        print('Closing...')
        time.sleep(0.5)
        cmd_clean()
        sys.exit()
    else:
        cmd_clean()
        exit()

def exit():
    print(Back.RED)
    x = input('Type y(yes)/n(no) or press Enter(no): ')
    cmd_clean()
    if x == 'y' or x =='Y':
        calculation()
        more_operations()
    elif x == 'n' or x =='N' or x == '':
        print(Back.CYAN)
        print('Closing...')
        time.sleep(0.5)
        cmd_clean()
        sys.exit()
    else:
        cmd_clean()
        exit()

calculation()
more_operations()
