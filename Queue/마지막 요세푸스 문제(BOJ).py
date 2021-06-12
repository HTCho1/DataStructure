# BOJ 1179
from collections import deque
import sys
sys.setrecursionlimit(10000)

n, k = map(int, sys.stdin.readline().rstrip().split())

def Josephus(n, k):
    if n == 1: return 0
    if k == 1: return n - 1
    if k <= n:
        n_ = n - n // k
        ret = Josephus(n_, k) - n % k
        if ret < 0: ret += n_
        return (k * (ret % n_)) // (k - 1)
    else:
        return (Josephus(n - 1, k) + k) % n

print(Josephus(n, k) + 1)