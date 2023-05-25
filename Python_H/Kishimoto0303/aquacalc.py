#datetimeをimport
from datetime import date

#引数を取得
import sys
args = sys.argv

#引数を代入
datestring = args[1]
adult    = int(args[2])
children = int(args[3])

#曜日判定
year = int(datestring[0:4])
manth = int(datestring[4:6])
day = int(datestring[6:8])
dt = date(year, manth, day)

# #合計値変数
total = 0

# #曜日変数
weekday_decision = dt.strftime("%a") 

if (weekday_decision == "Sat" or weekday_decision == "Sun"):
    #土日の合計値計算
    total = adult * 2400 + children * 1500
else:
    #平日の合計値計算
    total = adult * 2000 + children * 1200

#計算結果出力
print(total,end="")
