import sys
args = sys.argv

add_posi = int(args[1])
add_name = args[2]

animal = ["giraffe", "tiger","zebra", "elephant", "lion"]

animal.insert(add_posi-1,add_name)
animal.pop
print(animal)
animal.sort()
print(animal)