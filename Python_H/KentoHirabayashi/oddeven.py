import sys

# input value
args = sys.argv
num = int(args[1])

# output "even" or "odd"
print("偶数" if num % 2 == 0 else "奇数", end="")