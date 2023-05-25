import sys
args = sys.argv

#引数を変数に代入
num = int(args[1])

#合計値を格納する
total = num

while total < 100 and total > 0:
    total = total + num

if total == 100:
    print("Just 100!", end="")
else:
    print("Over!",end="")
