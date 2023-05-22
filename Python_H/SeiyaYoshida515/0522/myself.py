import introduce as intro
#引数を受け取るための設定
import sys
args = sys.argv

name = args[1]
age = args[2]

#引数を用いたインスタンスの作成
human = intro.Intro(name, age)
print(human.name_out())
print(human.age_out())