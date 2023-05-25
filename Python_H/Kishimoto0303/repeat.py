#引数を受け取る
import sys
args = sys.argv
num = int(args[1])

total = num

while total < 100 and total > 0:
    total += num

if total == 100:
    print("Just 100!", end="")
else:
    print("Over!", end="")