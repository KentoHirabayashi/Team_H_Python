#引数を受け取るための設定
import sys
args = sys.argv
num = int(args[1])

#引数で指定した分繰り返し出力
for i in range(1,num+1):
    print("ひつじが{0}匹".format(i))