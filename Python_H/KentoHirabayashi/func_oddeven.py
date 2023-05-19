import sys

args = sys.argv

def even_odd_decision(num):
    if num % 2 == 0:
        return "偶数"
    else:
        return "奇数"

def calcvalue(values):
    for value in values:
        print(f"{value}は{even_odd_decision(value)}")


# input values
values = list(map(int, args[1:]))

calcvalue(values)
