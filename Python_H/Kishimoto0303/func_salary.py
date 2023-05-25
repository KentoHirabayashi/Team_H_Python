#decimal関数を呼び出し
from decimal import Decimal, ROUND_HALF_UP

#calcsalary関数
def calcsalary(salary):
    
    #taxを定義
    tax = 0

    #税率計算
    if salary > 1000000 :
        #100万以上の場合の税率計算
        tax = (salary - 1000000 )* 0.2 + (1000000 * 0.1 )
    else:
        #100万以下の場合の税率計算
        tax = salary * 0.1

    #税額は小数第一位を四捨五入し、整数とする
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

    #支給額計算
    pay_amount = salary - tax

    #戻り値としてpay_amount,taxを指定
    return pay_amount,tax

