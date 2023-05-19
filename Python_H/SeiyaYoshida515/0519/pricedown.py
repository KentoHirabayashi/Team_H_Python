import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]          #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")      #果物類をタプルで定義
alcohol = ("ビール", "日本酒")               #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く
ja_en = {"果物類":fruits, "酒類":alcohol, "麺類":noodles}
#print(ja_en.keys())

for i in ja_en.keys():
    if i == hm_class:
        #print(ja_en[i])
        #exit()
        for j in ja_en[i]:
            #print(j)
            if hinmoku[j] - price_down < 1:
                hinmoku[j] = 1
            else:
                hinmoku[j] -= price_down
            #print(hinmoku[j])

print(hinmoku,end="")