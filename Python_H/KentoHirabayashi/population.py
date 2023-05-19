import sys

args = sys.argv

# input food name
index = int(args[1])
index -= 1

population_list = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")
if index < len(population_list):
    print(population_list[index], end="")
else:
    print("範囲内の値を指定して下さい")