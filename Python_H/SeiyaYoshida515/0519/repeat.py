#引数を受け取るための設定
import sys
args = sys.argv
num = int(args[1])

#合計値を格納する変数totalの宣言
total = num

#totalが100以上になるまで足し合わせる処理
while total < 100 and total > 0:
    total += num

#totalがちょうど100かの判定
if total == 100:
    print("Just 100!", end="")
else:
    print("Over!", end="")