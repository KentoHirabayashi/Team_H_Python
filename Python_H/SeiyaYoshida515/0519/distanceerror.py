#引数を受け取るための設定
import sys
args = sys.argv

sta_name = [args[1], args[2]]
station = {"東京":0.0, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35}

#距離の大きい方から小さい方を引く処理
try:
    if station[sta_name[0]] > station[sta_name[1]]:
        distance = station[sta_name[0]] - station[sta_name[1]]
    else:
        distance = station[sta_name[1]] - station[sta_name[0]]
    #表示
    print(round(distance,2), end="")
except:#例外処理
    print("のぞみの停車駅を引数に設定してください", end="")
