import sys
args = sys.argv

# 引数から変数に各教科の点数を代入
math = int(args[1])
japanese = int(args[2])
english = int(args[3])

if (math >= 70 and japanese >= 70 and english >= 70):
    print("合格", end="")
else:
    if (math + japanese + english >= 220):         
        if (math >= 50 and japanese >= 50 and english >= 50):   
            print("合格", end="")  
        else:
            print("不合格", end="")
    else:
        print("不合格", end="")
          