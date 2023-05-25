from datetime import datetime
from database import session
from tables import Holiday

import sys
args = sys.argv

input_date = str(args[1]) # 日付、文字列 
adult_num = int(args[2]) # 大人の人数
child_num = int(args[3]) # 子供の人数

dt = datetime.strptime(input_date, "%Y%m%d") # 5行目の文字列→日付(20XX, XX, XX)
weekday = datetime.strftime(dt,"%a")           # 日付→文字列（曜日）

public_holiday = session.query(Holiday).filter_by(holi_date=dt).first() #祝日かどうかの説明

#土日か祝日の時
if weekday == 'Sat' or weekday == 'San' or public_holiday != None:
    #大人2400、子供1500
    adult_fee = 2400 * adult_num
    child_fee = 1500 * child_num

#平日の時
else:
    #大人2000、子供1200
    adult_fee = 2000 * adult_num
    child_fee = 1200 * child_num

sum = adult_fee + child_fee
print(sum, end="")