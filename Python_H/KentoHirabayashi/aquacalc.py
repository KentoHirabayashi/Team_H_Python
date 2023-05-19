from datetime import date
import sys
import re


args = sys.argv

#引数を変数に代入
input_date = args[1]
adult = int(args[2])
child = int(args[3])

#create data object
## splite date
pattern = r"(\d{4})(\d{2})(\d{2})"
splite_date = re.search(pattern, input_date)
year, month, day = splite_date.groups()
## create date object
dt = date(int(year), int(month), int(day))

#休日料金
if dt.weekday() >= 5:
    pay = 2400 * adult + 1500 * child
#平日料金
else:
    pay = 2000 * adult + 1200 * child

#合計金額の出力
print(pay, end="")