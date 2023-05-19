import sys
args = sys.argv

sen = args[1]
num = args[2]

sen = sen.split()

print(sen[int(num)-1],end="")