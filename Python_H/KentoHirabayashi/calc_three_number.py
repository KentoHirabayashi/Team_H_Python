import sys

args = sys.argv

# 入力した値を整数型に変換し、リストに入力する
input_numbers = list(map(int, args[1:4]))
# リストの中の合計値を求める
result = sum(input_numbers)

print(result, end="")