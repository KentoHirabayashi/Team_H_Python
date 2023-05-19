try:
    import sys
    args = sys.argv

    #引数を変数に代入
    nam = args[1],args[2]

    distance = {
        "東京": 0.00, "品川":6.78, "新横浜":25.54, "名古屋":342.02, "京都":476.31, "新大阪":515.35
    }

    if distance[nam[0]] > distance[nam[1]]:
        result =  distance[nam[0]] - distance[nam[1]]
    else:
        result = distance[nam[1]] - distance[nam[0]]

    print(round(result,2),end="")
except:
    print("のぞみの停車駅を引数に設定してください",end="")