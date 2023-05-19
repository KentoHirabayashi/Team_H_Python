import sys
args = sys.argv

#引数を変数に代入
nam = args[1], int(args[2])
ing = nam[0].split(" ") 
print(ing[nam[1]- 1],end="")