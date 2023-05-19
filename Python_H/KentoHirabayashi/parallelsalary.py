import sys

from func_salary import calc_salary


def parallel_salary(salaries):
    for salary in salaries:
        pay_amount, tax_amount = calc_salary(salary)
        print(f"給与:{ salary }、支給額:{round(pay_amount)}、税額:{round(tax_amount)}")

args = sys.argv
salaries = list(map(int, args[1:]))

parallel_salary(salaries)

