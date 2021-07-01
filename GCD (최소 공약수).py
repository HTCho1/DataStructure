# a, b를 빼면서 gcd를 구하는 함수
def gcd_sub(a, b):
    while a * b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a + b

# a, b를 나누면서 gcd를 구하는 함수
def gcd_mod(a, b):
    while a * b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

# 재귀함수로 gcd를 구하는 함수
def gcd_rec(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_rec(b, a % b)


# a, b를 입력받는다
a, b = map(int, input().split())
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
x = gcd_sub(a, b)
y = gcd_mod(a, b)
z = gcd_rec(a, b)

print(x, y, z)