from introduce import Intro

class IntroFam(Intro):
    def __init__(self, name, age, cat): # コンストラクタ（初期化メソッド）。たい焼きの型を温める
        self.name = name
        self.age = age
        self.cat = cat

    #猫  
    def cat_out(self):
        cattxt = "飼い猫の名前は、{0}です".format(self.cat)
        return cattxt 
    
# __init__()メソッド
# インスタンス生成時にこのメソッドが自動的に実行され、勝手に初期化してくれる