from decimal import Decimal, ROUND_HALF_UP
import sys

args = sys.argv

salary = int(args[1])

if salary <= 1000000:
    tax_rate = 0.1
    tax = salary * tax_rate
    
    #print("I don't like {}".format(food), end="")
else:
    tax_rate = 0.2
    tax = (1000000 * 0.1) + (salary - 1000000) * tax_rate

tax = Decimal(str(tax)).quantize(Decimal("0"),
rounding=ROUND_HALF_UP)
pay_amount = salary - tax
print("支給額:{0}、税額:{1}".format(pay_amount, tax), end="")
#print("支給額:"+ str(pay) + "、税額:" + str(tax), end="")