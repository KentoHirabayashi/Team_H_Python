import sys
args = sys.argv

#引数を数学に代入
ma = int(args[1])
#引数を国語に代入
jp = int(args[2])
#引数を英語に代入
eng = int(args[3])

if (ma >= 70 and jp >= 70 and eng >= 70) or (ma + jp + eng >= 220):
    if (ma >= 50 and jp >= 50 and eng >= 50):
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")
