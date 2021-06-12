import sys

operator = ['+', '-', '*', '/']
bracket = ['(', ')']

def operator_priority(input):
    if input in '*/':
        return 1
    elif input in '+-':
        return 0

def InFixToPostFix(input):
    postfix, opstack = [], []
    for token in input:
        if token not in operator and token not in bracket:
            postfix.append(token)
        elif token == '(':
            opstack.append(token)
        elif token == ')':
            while True:
                a = opstack.pop()
                if a == '(':
                    break
                postfix.append(a)
        elif token in operator:
            p = operator_priority(token)
            while len(opstack) > 0:
                top = opstack[-1]
                if top == '(':
                    top = '+'
                if operator_priority(top) <= p:
                    break
                postfix.append(opstack.pop())
            opstack.append(token)
    #print(opstack)
    while len(opstack) > 0:
        postfix.append(opstack.pop())
    return postfix

def Calculator(postfix):
    lst = []
    for token in postfix:
        print(lst)
        if token not in operator and token not in bracket:
            lst.append(token)
        if token == '+':
            a = lst.pop()
            b = lst.pop()
            lst.append(int(b) + int(a))
        elif token == '-':
            a = lst.pop()
            b = lst.pop()
            lst.append(int(b) - int(a))
        elif token == '*':
            a = lst.pop()
            b = lst.pop()
            lst.append(int(b) * int(a))
        elif token == '/':
            a = lst.pop()
            b = lst.pop()
            lst.append(int(b) / int(a))
    return lst

input_list = list(sys.stdin.readline().rstrip())
#print('input_list: ', input_list)
postfix = InFixToPostFix(input_list)
print(postfix)
result = Calculator(postfix)
print(result[0])