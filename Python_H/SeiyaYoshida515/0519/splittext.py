#引数を受け取るための設定
import sys
args = sys.argv

En_list = args[1].split(" ")
print(En_list[int(args[2])-1], end="")