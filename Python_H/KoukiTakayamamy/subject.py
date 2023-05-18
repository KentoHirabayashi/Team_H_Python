import sys
args = sys.argv

a = args[1]
b = args[2]
c = args[3]

ma = int(a)
ja = int(b)
en = int(c)

sum = ma + ja + en

if(70 <= ma <=100) and (70 <= ja <=100) and (70 <= en <=100):

    print("合格", end="")

else:
    
    if(sum >= 220) and (50 <= ma <=100) and (50 <= ja <=100) and (50 <= en <=100):
        print("合格", end="")

    else:
        print("不合格", end="")
