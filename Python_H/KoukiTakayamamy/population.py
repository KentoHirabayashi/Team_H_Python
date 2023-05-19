import sys
args = sys.argv

population_list = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

rank_num = int(args[1])

print(population_list[rank_num-1],end="")