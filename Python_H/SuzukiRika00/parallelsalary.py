import funk_salary
import sys

args = sys.argv

salaries = (int(args[1]), int(args[2]), int(args[3]))


for i in salaries:
    num = funk_salary.calcsalary(i)
    print("給与:{0}、支給額:{1}、税額:{2}".format(salaries, num[0], num[1]))
