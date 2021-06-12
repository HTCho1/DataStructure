# Stack을 이용하여 괄호 맞추기
import sys

input_data = list(sys.stdin.readline().rstrip())

def correctBracket(input_data):
    stack = []
    for input in input_data:
        if input == '(': stack.append(input)
        elif input == ')' and len(stack) != 0: stack.pop()
        elif input == ')' and len(stack) == 0: return [None]
    return stack

answer = correctBracket(input_data)

if len(answer) == 0:
    print(True)
else:
    print(False)
