import sys

args = sys.argv

# 入力した値を整数型に変換し、リストに入力する
input_numbers = list(map(int, args[1:4]))
# リストの中の合計値を求める
sum_result = sum(input_numbers)

# 各条件のBooleanを格納
is_over_220 = sum_result >= 220
is_all_70_over = input_numbers[0] >= 70 and  input_numbers[1] >= 70 and input_numbers[2] >= 70
is_not_50_under = not(input_numbers[0] < 50 or  input_numbers[1] < 50 or input_numbers[2] < 50)


if (is_over_220 or is_all_70_over) and (is_not_50_under):
    print("合格", end="")
else:
    print("不合格", end="")
