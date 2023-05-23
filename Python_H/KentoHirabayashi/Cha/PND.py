import sys

args = sys.argv
n = int(args[1])

result = []

explore_range = int(n**0.5)

for i in range(2, explore_range + 1):
    while True:
        if n%i == 0:
            result.append(i)
            n = n // i
        else:
            break

if  n > 1:
    result.append(n)

print(result, end="")