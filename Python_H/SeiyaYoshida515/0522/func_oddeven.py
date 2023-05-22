#引数を受け取るための設定
import sys
args = sys.argv
num_list = args[1:]

def calcvalue(num):
    if num % 2 == 0:
        print("{0}は偶数".format(num), end="\n")
    else:
        print("{0}は奇数".format(num), end="\n")

for i in num_list:
    calcvalue(int(i))