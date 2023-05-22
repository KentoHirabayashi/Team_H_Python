import sys

args = sys.argv

# input food name
departure_station = args[1]
arrival_station = args[2]

station_distance = {
    "東京": 0.00,
    "品川": 6.78,
    "新横浜": 25.54,
    "名古屋": 342.02,
    "京都": 476.31,
    "新大阪": 515.35
}


try:
    station_distance_value = abs(station_distance[arrival_station] - station_distance[departure_station])

    print(f"{station_distance_value:.2f}", end="")
except:
    print("のぞみの停車駅を引数に設定してください", end="")