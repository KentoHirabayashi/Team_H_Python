import datetime
import sys
args = sys.argv

input_date = str(args[1]) #日付、文字列 
adult_num = int(args[2]) #人数
child_num = int(args[3]) #人数

dt = datetime.datetime.strptime(input_date, "%Y%m%d") # 5行目の文字列→日付(20XX, XX, XX)
youbi = datetime.datetime.strftime(dt,"%a")           #日付→文字列（曜日）
# print(youbi)
#土日
if youbi == 'Sat' or youbi == 'San':
    #大人2400、子供1500
    adult_fee = 2400 * adult_num
    child_fee = 1500 * child_num
else:
    #大人2000、子供1200
    adult_fee = 2000 * adult_num
    child_fee = 1200 * child_num

sum = adult_fee + child_fee
print(sum, end="")