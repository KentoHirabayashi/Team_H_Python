import sys

args = sys.argv

# input index and animal name
index = int(args[1])
animal_name = args[2]

animal_name_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

# practice1: add animal name
animal_name_list.insert(index, animal_name)

# practice2: remove last item
animal_name_list.pop()

# practice3: sort in ascending order
animal_name_list.sort()
print(animal_name_list, end="")