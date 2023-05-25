import sys
from decimal import Decimal, ROUND_HALF_UP
import func_salary

args = sys.argv

#給与を変数に代入
salary1 = int(args[1])
salary2 = int(args[2])
salary3 = int(args[3])

pay_amount1,tax1 = func_salary.calcsalary(salary1)
pay_amount2,tax2 = func_salary.calcsalary(salary2)
pay_amount3,tax3 = func_salary.calcsalary(salary3)

#結果出力
print("支給額:" + str(pay_amount1) + "税額:" + str(tax1))
print("支給額:" + str(pay_amount2) + "税額:" + str(tax2))
print("支給額:" + str(pay_amount3) + "税額:" + str(tax3))