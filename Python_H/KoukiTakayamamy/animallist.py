import sys
args = sys.argv

animallist = ["giraffe", "tiger", "zebra", "elephant", "lion"]

input_index = int(args[1])
input_animal = args[2]

animallist.insert(input_index,input_animal)

del animallist[-1]

animallist.sort()

print(animallist,end="")