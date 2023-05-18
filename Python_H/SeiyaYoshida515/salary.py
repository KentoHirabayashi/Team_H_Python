#sysモジュールをインポート
import sys
from decimal import Decimal, ROUND_HALF_UP

#argsに引数を格納、salaryに第一引数を格納
args = sys.argv
salary = int(args[1])

#給与から税額を計算
if salary >= 1000000:
    tax = 100000 + (salary-1000000) * 0.2
else:
    tax = salary * 0.1

#税額を四捨五入
tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

#支給額を計算
after_tax_pay = salary - tax

#支給額、税額を出力
print("支給額:{0}、税額:{1}".format(after_tax_pay, tax), end="")

