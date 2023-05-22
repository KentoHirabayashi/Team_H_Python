import sys
args = sys.argv

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

def multi_calcvalue(values):
    for value in values:
        calcvalue(value)


# input values
values = list(map(int, args[1:]))

multi_calcvalue(values)
