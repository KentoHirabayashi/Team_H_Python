#引数を取得
import sys
args = sys.argv

#引数をvalに代入
val = int(args[1])
#valを2で割る処理
if val % 2 == 0:
    print("偶数", end="")
else:
    print("奇数", end="")
