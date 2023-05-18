import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv

payroll_amount = int(args[1])

if(payroll_amount > 1000000):
    tax = 100000 + (payroll_amount - 1000000) * 0.2



else:
    tax = payroll_amount *0.1


tax_amount = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

pay_amount = payroll_amount - tax_amount

print("支給額:{0}、税額:{1}".format(pay_amount,tax_amount), end="")

