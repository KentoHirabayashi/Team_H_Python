import os
path = os.path.join("../../files/sheep.txt")

a_file = open(path, mode="w", encoding="utf-8")
try:
    import sys
    args = sys.argv

    #引数を変数に代入
    val = int(args[1])

    for i in range(val):
        a_file.write("ひつじが" + str(i + 1) + "匹" + "\n")

finally:
#ファイル閉じる
    a_file.close()