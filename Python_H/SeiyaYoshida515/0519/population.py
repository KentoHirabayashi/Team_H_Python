#引数を受け取るための設定
import sys
args = sys.argv

#国別人口ランキングをタプルで作成
country_rank = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

#引数に応じた国名出力
print(country_rank[int(args[1])-1], end="")