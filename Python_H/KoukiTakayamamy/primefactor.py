import sys

args = sys.argv

n = args[1]


def primefactor(n):
    ar = []
    temp = n
    for i in range(2, int(n ** 0.5) + 1):
        while temp % i == 0:
            temp //= i
            ar.append(i)

    if temp != 1:
        ar.append(temp)

    if ar == []:
        ar.append(n)

    return ar

result = primefactor(int(n)) 

print(result)