import sys

args = sys.argv

num = args[1]

if int(num) %2 == 1:
    print("奇数", end="")
else:
    print("偶数", end="")
