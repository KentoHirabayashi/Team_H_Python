from datetime import date

#引数を受け取るための設定
import sys
args = sys.argv
#引数を変数に格納
date_str = args[1]
adult_num = int(args[2])
child_num = int(args[3])
#日付をリスト化
date_list = [int(date_str[:4]), int(date_str[4:6]), int(date_str[6:8])]
#dateクラスに格納
date_tmp = date(date_list[0], date_list[1], date_list[2])
day_of_week = date_tmp.weekday()#曜日変換（月：0, ～ 日:6）

#祝日判定
#holiday = session.query(Holiday).filter_by(holi_date=date(date_list[0], date_list[1], date_list[2])).first()

#金額計算
if day_of_week == 5 or day_of_week == 6 :#土日祝日の時
    total = adult_num * 2400 + child_num * 1500
else:
    total = adult_num * 2000 + child_num * 1200

#出力
#print("合計金額は{0}円です".format(total))
print(total,end="")