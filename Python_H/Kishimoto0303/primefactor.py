#引数取得
import sys
args = sys.argv

num = int(args[1])

def prime_factorize(num):
    a = []
    while num % 2 == 0:
        a.append(2)
        num //= 2
    f = 3
    while f * f <= num:
        if num % f == 0:
            a.append(f)
            num //= f
        else:
            f += 2
    if num != 1:
        a.append(num)
    return a

print(prime_factorize(num), end="")