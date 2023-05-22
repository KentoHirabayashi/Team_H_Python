#sysモジュールをインポート
import sys
import func_salary

#argsに引数を格納、salaryに第一引数を格納
args = sys.argv
salary = args[1:]

for i in salary:
    pay_tax = func_salary.calcsalary(int(i))
    #支給額、税額を出力
    print("支給額:{0}、税額:{1}".format(pay_tax[0],pay_tax[1]), end="\n")

