#引数を受け取るための処理
import sys
args = sys.argv

#各教科の変数に点数を格納
Ma = int(args[1])
Ja = int(args[2])
En = int(args[3])

#合格判定
if (Ma >= 70 and Ja >=70 and En >= 70) or Ma + Ja + En >=220:
    if Ma >= 50 and Ja >= 50 and En >= 50:
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")