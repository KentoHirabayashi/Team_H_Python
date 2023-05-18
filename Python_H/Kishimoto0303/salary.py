import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

#給与を変数に代入
salary = int(args[1])
#税額計算
if salary > 1000000 :
    tax = 100000 + (salary - 1000000) * 0.2
else:
    tax = salary * 0.1

tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

#支給額計算
pay_amount = salary - tax

print("支給額:" + str(pay_amount) + "、" +"税額:" + str(tax), end="")