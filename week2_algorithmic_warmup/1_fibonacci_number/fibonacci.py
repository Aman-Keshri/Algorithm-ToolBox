# Uses python3
def calc_fib(n,l):
    for i in range(2,n):
        l[i] = l[i-1] + l[i-2]
    return l[n-1]

n = int(input())
l = [0] * n
l[0] = 0
l[1] = 1
print(calc_fib(n,l))
