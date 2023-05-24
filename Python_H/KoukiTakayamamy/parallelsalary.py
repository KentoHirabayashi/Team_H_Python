import func_salary
import sys

args = sys.argv

salarys = (int(args[1]),int(args[2]),int(args[3]))


for i in range(3):
    im = func_salary.calc_salary(salarys[i])

    print(f"給与:{salarys[i]}、支給額:{im[0]}、税額:{im[1]}")
