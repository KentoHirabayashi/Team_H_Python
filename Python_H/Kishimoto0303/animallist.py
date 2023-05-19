import sys
args = sys.argv

#引数を変数に代入
nam = int(args[1])
#動物名リスト
animals = [ "giraffe", "tiger", "zebra", "elephant", "lion"]

#値を挿入
animals.insert(nam, args[2])

#リストの末尾削除
animals.pop()

#リストを昇順に並び替え
animals.sort()

print(animals, end="")
