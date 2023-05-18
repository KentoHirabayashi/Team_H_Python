import sys

args = sys.argv

input_number1 = args[1]

if int(input_number1) %2 == 1:
    print("奇数", end="")
else:
    print("偶数", end="")
