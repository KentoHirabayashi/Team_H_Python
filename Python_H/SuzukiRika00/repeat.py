import sys

args = sys.argv

num = int(args[1])
sum = 0

while True:
    sum = sum + num
    if sum == 100:
        print("Just 100!", end="")
        break
    if sum > 100:
        print("Over!", end="") 
        break





