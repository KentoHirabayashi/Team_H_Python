import sys
args = sys.argv

rank = int(args[1])

ranking = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

rank = rank - 1

print(ranking[rank], end="")