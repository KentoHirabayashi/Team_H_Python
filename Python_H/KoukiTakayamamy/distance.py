import sys
args = sys.argv

distances = {"東京":0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}

select1 = str(args[1])
select2 = str(args[2])

select1_distance = distances[select1]
select2_distance = distances[select2]

result = select1_distance - select2_distance

if(result < 0):
    result = -result

print(round(result,2),end="")