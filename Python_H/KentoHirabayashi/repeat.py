import sys

args = sys.argv

# input food name
loop_count = int(args[1])

sum_result = 0
while(True):
    sum_result += loop_count

    if sum_result == 100:
        print(f"Just 100!", end="")
        break
    elif sum_result > 100:
        print("Over!", end="")
        break
