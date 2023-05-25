import sys
args = sys.argv
num = [args[1],args[2],args[3]]

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")

calcvalue(int(num[0]))
calcvalue(int(num[1]))
calcvalue(int(num[2]))