from decimal import Decimal, ROUND_HALF_UP
import sys
args = sys.argv

def calcsalary(salary):
    if salary <= 1000000:
        tax_rate = 0.1
        tax = salary * tax_rate
    
    else:
        tax_rate = 0.2
        tax = (1000000 * 0.1) + (salary - 1000000) * tax_rate

    tax = Decimal(str(tax)).quantize(Decimal("0"),
    rounding=ROUND_HALF_UP)

    pay_amount = salary - tax
                                     
    return (pay_amount, tax)