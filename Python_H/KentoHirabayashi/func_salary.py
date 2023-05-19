def calc_salary(salary):
    pay_amount = 0
    tax_amount = 0

    if salary < 100_0000:
        # 10%で計算を行う
        tax_amount += salary * 0.1
        
    else:
        # 20%で計算を行う
        tax_amount += (salary - 100_0000) * 0.2
        # 100万円に掛かる税額を足し合わせる
        tax_amount += 100000

    # 支給額を計算する
    pay_amount = salary - tax_amount
    return pay_amount, tax_amount