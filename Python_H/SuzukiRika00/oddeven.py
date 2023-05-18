import sys

args = sys.argv

input = args[1]
num = int(input)
#input = int(args[1])でも可

if num %2 == 1:
    print("奇数", end="")
else:
    print("偶数", end="")
