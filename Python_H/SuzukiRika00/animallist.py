import sys
args = sys.argv

num = int(args[1])
animal = args[2]

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]
animals.insert(num, animal)
del animals[-1]

animals.sort(key=None, reverse=False) #Falseで昇順
print(animals, end="")
