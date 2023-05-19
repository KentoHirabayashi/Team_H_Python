#引数を受け取るための設定
import sys
args = sys.argv

#引数を変数に格納
add_posi = int(args[1])
add_name = args[2]

#リストを定義
animal = ["giraffe", "tiger","zebra", "elephant", "lion"]

#リストの操作
animal.insert(add_posi,add_name)
animal.pop()
animal.sort()

#表示
print(animal, end="")