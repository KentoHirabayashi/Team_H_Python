import sys
args = sys.argv

sum = 0
i = 0

while True:
    
    sum += int(args[1])
    i += 1
    if(sum == 100):
        print("Just 100!",end="")
        break

    if(sum > 100):
        print("Over!",end="")
        break
    
    

