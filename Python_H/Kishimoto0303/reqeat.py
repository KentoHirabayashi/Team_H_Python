import sys
args = sys.argv

#引数を変数に代入
val = args[1]

#合計値
total = 0

while True:
    val += total
    if val == 100:
       print("Just 100!")
       break
    elif val >= 100:
         print("Over!")
         break