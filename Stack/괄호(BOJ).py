# BOJ 9012
import sys

T = int(sys.stdin.readline().rstrip())

def solution(input):
    stack = []
    for i in input:
        if i == '(':
            stack.append(i)
            continue
        if i == ')' and len(stack) ==0:
            return False
        stack.pop()
    if len(stack) > 0:
        return False
    return True

for i in range(T):
    input_data = list(sys.stdin.readline().rstrip())
    result = solution(input_data)
    if result:
        print('YES')
    else:
        print('NO')