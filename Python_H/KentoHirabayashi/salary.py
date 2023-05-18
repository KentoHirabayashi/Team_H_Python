import sys


args = sys.argv

input_numbers = int(args[1])

pay_amount = 0
tax_amount = 0

if input_numbers < 100_0000:
    # 10%で計算を行う
    tax_amount += input_numbers * 0.1
    
else:
    # 20%で計算を行う
    tax_amount += (input_numbers - 100_0000) * 0.2
    # 100万円に掛かる税額を足し合わせる
    tax_amount += 100000

pay_amount = input_numbers - tax_amount
print(f"支給額:{round(pay_amount)}、税額:{round(tax_amount)}")