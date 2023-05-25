#引数を取得
import sys
args = sys.argv

#引数を数学の得点maに代入
ma = int(args[1])
#引数を国語の得点jpに代入
jp = int(args[2])
#引数を英語の得点enに代入
en = int(args[3])

#3教科とも70点以上、または、合計点数が220点以上 
if (ma >= 70 and jp >= 70 and en >= 70) or (ma + jp + en >= 220):
    #1科目も50点未満がない
    if (ma >= 50 and jp >= 50 and en >= 50):
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")