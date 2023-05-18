import sys

args = sys.argv

input_numbers = list(map(int, args[1:4]))
result = sum(input_numbers)
print(result, end="")