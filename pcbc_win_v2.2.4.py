from colorama import init
import time
import os
import sys
from colorama import Back, Style
init()

upper_sym = '-'
sq_root = '\u221a'

def cmd_clean():
    print(Style.RESET_ALL)
    os.system('cls')
    print(Style.RESET_ALL)

def first_op():
    print(Style.RESET_ALL, end = '')
    print('      ','-------------')
    print('      ','| ', end = '')
    print(Back.CYAN, end = '')
    print(' ?',' ?',' ? ', end = '')
    print(Style.RESET_ALL, end = '')
    print(' |')
    print('      ','-------------')
    try:
        print(Back.CYAN)
        global a
        a = input(' Enter the first number: ')
        cmd_clean()
        float(a)
    except:
        cmd_clean()
        print(Back.RED, end = '')
        print('' , a, 'is not a number ')
        print(' Select a num type value ')
        print('')
        del a
        time.sleep(0.5)
        first_op()

    test = int(0)
    global first_v
    first_v = None
    first_v = int(0)
    if float(a) == float(test):
        first_v = 0
    else:
        first_v = a
    float(first_v)

    global first_len
    first_len = None
    if first_v == 0:
        first_len = 1
    else:
        first_len = len(first_v)

    try:
        global first_zerof
        first_zerof = False
        global fminus_trig
        fminus_trig = False
        global count1
        count1 = 0
        if first_v[first_len-1] == '.':
            first_len = first_len - 1
        for i in range(first_len):
            if first_v[i] == str(0) and first_len != 1:
                count1 = count1 + 1
            elif first_v[i] == str('.'):
                count1 = count1 - 1
                break
            elif first_v[i] == '-':
                count1 = count1 + 1
                fminus_trig = True
                continue
            else:
                break
    except:
        count1 = 0
        first_v = 0
        first_zerof = True

    global first_up_line
    global first_down_line
    global zero_down_line
    first_len = first_len-count1
    if fminus_trig is True:
        first_up_line = (first_len + 1) * '-'
        first_down_line = (first_len + 1) * upper_sym
    else:
        first_up_line = first_len * '-'
        first_down_line = first_len * upper_sym
    zero_down_line = 12 * upper_sym

def oper_c():
    global symb
    print(Style.RESET_ALL, end = '')
    print('      ','---' + first_up_line + '---------')
    print('      ','| ', end = '')
    print(Back.CYAN, end = '')
    try:
        if fminus_trig is True:
            print('', '-' + first_v[count1:first_len+count1], ' ?', ' ? ', end = '')
        else:
            print('', first_v[count1:first_len+count1], ' ?', ' ? ', end = '')
    except:
        print('', '0', ' ?', ' ? ', end = '')
    print(Style.RESET_ALL, end = '')
    print(' |')
    print('      ',first_down_line + zero_down_line)
    print(Back.CYAN)
    print('   |  +  |  -  |  *  |  /  |   ')
    print('   |  %  | %of |  ** | sqr |   ')
    print('')
    print(' (% - Modulus, ** - Exponent   ')
    print(' %of - Percentage, sqr - 2',sq_root,') ')
    print('')
    symb = input(' Choose the operator: ')
    cmd_clean()
    if symb == '+' or symb == '-' or symb == '*' or symb == '/' or symb == '%' or symb == '%of' or symb == '**' or symb == 'sqr':
        oper = True
        if symb == 'sqr':
            res = float(first_v) ** 0.5
            print(Style.RESET_ALL, end = '')
            print('      ','-----------' + first_up_line)
            print('      ','| ', end = '')
            print(Back.CYAN, end = '')
            try:
                if fminus_trig is True:
                    print('',sq_root, 'of', '-' + first_v[count1:first_len+count1],'', end = '')
                else:
                    print('',sq_root, 'of', first_v[count1:first_len+count1],'', end = '')
            except:
                print('',sq_root, 'of', '0','', end = '')
            print(Style.RESET_ALL, end = '')
            print(' |')
            print('      ',first_down_line + '-----------')
            print(Back.GREEN)
            print('The answer is: ', round(res, 13), '')
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
        print('         Wrong operator        ')
        oper = False
    if oper is False:
        print('  Select the correct operator  ')
        print('')
        time.sleep(0.5)
        oper_c()

def sec_op():
    print(Style.RESET_ALL, end = '')
    print('      ','--' + first_up_line + sec_up_line + '---------')
    print('      ','| ', end = '')
    print(Back.CYAN, end = '')
    try:
        if fminus_trig is True:
            print('', '-' + first_v[count1:first_len+count1],'', symb, ' ? ', end = '')
        else:
            print('', first_v[count1:first_len+count1],'', symb, ' ? ', end = '')
    except:
        print('', '0','', symb, ' ? ', end = '')
    print(Style.RESET_ALL, end = '')
    print(' |')
    print('      ',first_down_line + sec_down_line + add1_down)
    print(Back.CYAN)
    try:
        global b
        b = input(' Enter the second number: ')
        cmd_clean()
        float(b)
    except:
        cmd_clean()
        print(Back.RED, end = '')
        print('', b, 'is not a number ')
        print(' Select a num type value ')
        print('')
        del b
        time.sleep(0.5)
        sec_op()

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

    try:
        global sec_zerof
        sec_zerof = False
        global sminus_trig
        sminus_trig = False
        global count2
        count2 = 0
        if second_v[sec_len-1] == '.':
            sec_len = sec_len - 1
        for i in range(sec_len):
            if second_v[i] == str(0) and sec_len != 1:
                count2 = count2 + 1
            elif second_v[i] == str('.'):
                count2 = count2 - 1
                break
            elif second_v[i] == '-':
                count2 = count2 + 1
                sminus_trig = True
                continue
            else:
                break
    except:
        count2 = 0
        second_v = 0
        sec_zerof = True

    global third_up_line
    global third_down_line
    global add2_down
    sec_len = sec_len-count2
    if sminus_trig is True:
        third_up_line = (sec_len + 1) * '-'
        third_down_line = (sec_len + 1) * upper_sym
    else:
        third_up_line = sec_len * '-'
        third_down_line = sec_len * upper_sym
    add2_down = 10 * upper_sym

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
        if res == 0:
            res = 0
        result()
    elif symb == '/':
        if second_v == 0:
            print(Style.RESET_ALL, end = '')
            print('      ','--' + first_up_line + sec_up_line + third_up_line + '--------')
            print('      ','| ', end = '')
            print(Back.CYAN, end = '')
            try:
                print('', first_v[count1:first_len+count1],'', symb,'', second_v[count2:sec_len+count2],'', end = '')
            except:
                if first_zerof is True and sec_zerof is True:
                    print('', '0','', symb,'', '0','', end = '')
                elif first_zerof is False and sec_zerof is True:
                    if fminus_trig is True:
                        print('', '-' + first_v[count1:first_len+count1],'', symb,'', '0','', end = '')
                    else:
                        print('', first_v[count1:first_len+count1],'', symb,'', '0','', end = '')
            print(Style.RESET_ALL, end = '')
            print(' |')
            print('      ',first_down_line + sec_down_line + third_down_line + add2_down)
            print(Back.RED, end = '')
            res = ' Cannot be divided by zero '
            print('')
            print(res)
            print('')
            more_operations()
        else:
            print(Back.CYAN, end = '')
            res = float(first_v) / float(second_v)
            if res == 0:
                res = 0
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
                print('     Result is too large     ')
                print(' Please choose another value ')
                print('')
                time.sleep(0.5)
                more_operations()

def result():
    print(Style.RESET_ALL, end = '')
    print('      ','--' + first_up_line + sec_up_line + third_up_line + '--------')
    print('      ','| ', end = '')
    print(Back.CYAN, end = '')
    try:
        if fminus_trig is True and sminus_trig is True:
            print('', '-' + first_v[count1:first_len+count1],'', symb,'', '-' + second_v[count2:sec_len+count2],'', end = '')
        elif fminus_trig is True and sminus_trig is False:
            print('', '-' + first_v[count1:first_len+count1],'', symb,'', second_v[count2:sec_len+count2],'', end = '')
        elif fminus_trig is False and sminus_trig is True:
            print('', first_v[count1:first_len+count1],'', symb,'', '-' + second_v[count2:sec_len+count2],'', end = '')
        else:
            print('', first_v[count1:first_len+count1],'', symb,'', second_v[count2:sec_len+count2],'', end = '')
    except:
        if first_zerof is True and sec_zerof is True:
            print('', '0','', symb,'', '0','', end = '')
        elif first_zerof is True and sec_zerof is False and sminus_trig is False:
            print('', '0','', symb,'', second_v[count2:sec_len+count2],'', end = '')
        elif first_zerof is True and sec_zerof is False and sminus_trig is True:
            print('', '0','', symb,'', '-' + second_v[count2:sec_len+count2],'', end = '')
        elif first_zerof is False and fminus_trig is False and sec_zerof is True:
            print('', first_v[count1:first_len+count1],'', symb,'', '0','', end = '')
        elif first_zerof is False and fminus_trig is True and sec_zerof is True:
            print('', '-' + first_v[count1:first_len+count1],'', symb,'', '0','', end = '')
    print(Style.RESET_ALL, end = '')
    print(' |')
    print('      ',first_down_line + sec_down_line + third_down_line + add2_down)
    print(Back.GREEN)
    print(' The answer is: ', round(res, 13), '')
    print('')

def more_operations():
    print(Back.CYAN, end = '')
    moreop = input(' One more operation?(y/n(Enter)): ')
    cmd_clean()
    while moreop == 'y' or moreop =='Y':
        calculation()
        print(Back.CYAN, end = '')
        moreop = input(' One more operation?(y/n(Enter)): ')
    if moreop == 'n' or moreop == 'N' or moreop == '':
        print(Back.CYAN)
        print(' Closing... ')
        time.sleep(0.5)
        cmd_clean()
        sys.exit()
    else:
        cmd_clean()
        exit()

def exit():
    print(Back.RED)
    x = input(' Type y(yes)/n(no) or press Enter(no): ')
    cmd_clean()
    if x == 'y' or x =='Y':
        calculation()
        more_operations()
    elif x == 'n' or x =='N' or x == '':
        print(Back.CYAN)
        print(' Closing... ')
        time.sleep(0.5)
        cmd_clean()
        sys.exit()
    else:
        cmd_clean()
        exit()

calculation()
more_operations()
