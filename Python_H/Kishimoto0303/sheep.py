import sys
args = sys.argv

#引数を変数に代入
val = int(args[1])

for i in range(val):
    print("ひつじが" + str(i + 1) + "匹")