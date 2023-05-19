import sys

args = sys.argv
departure_station = (args[1]) # 出発駅
arrival_station = (args[2]) # 到着駅

map ={
    '東京':0, '品川':6.78, '新横浜':25.54, 
    '名古屋':342.02, '京都':476.31, '新大阪':515.35 
}

try:
    distance = map[args[2]] - map[args[1]]
    print(abs(round(distance, 2)), end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")