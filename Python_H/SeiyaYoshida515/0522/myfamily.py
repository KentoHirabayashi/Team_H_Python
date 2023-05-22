import introfamily
#引数を受け取るための設定
import sys
args = sys.argv

name = args[1]
age = args[2]
cat_name = args[3]

#引数を用いたインスタンスの作成
human = introfamily.Introfam(name, age, cat_name)
print(human.name_out())
print(human.age_out())
print(human.cat_name_out())