import sys
args = sys.argv

#引数を変数に代入
nam = int(args[1])
country =("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(country[nam - 1],end = "")