class vendculc:
    def __init__(self) -> None:
        self.product = {
            "お茶": 110,
            "コーヒー": 100,
            "ソーダ": 160,
            "コンポタージュ": 130
        }
        self.money = 0
    
    def check_input_money(self, money):
        """
        投入金額が正当なものであるかを確認
        """
        self.money = money

        if self.money > 10_000:
            print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
            return False
        
        if min(self.product.values()) > self.money:
            print(min(self.product.values()))
            print(f"{self.money}円では購入できる商品がありません。再度投入金額を入力してください")
            return False
        
        if self.money % 10 != 0:
            print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
            return False
        
        return True
    
    def check_input_product(self, product_name):
        """
        入力された商品が購入可能かをチェックする
        """
        if product_name == "cancel":
            return False
        
        if self.product[product_name] > self.money:
            return False
        
        if self.product[product_name] <= self.money:
            self.money -= self.product[product_name]

            if  min(self.product.values()) > self.money:
                return False
            
        return True
    
    def print_able_list(self):
        """
        購入リストの表示
        """
        print("購入可能リスト")
        for product_name, price in self.product.items():
            if price <= self.money:
                print(f"{product_name}：{price}円")

    def print_product_list(self):
        """
        プロダクトリストの表示
        """
        for product_name, price in self.product.items():
            print(f"{product_name}：{price}円")
        

    def calc_change(self):
        """
        おつり計算
        """
        money_kinds = [5000, 1000, 500, 100, 50, 10]

        for money_kind in money_kinds:
            money_count = 0

            while self.money >= money_kind:
                self.money -= money_kind
                money_count += 1
            
            money_count and print(f"{money_kind}円: {money_count}枚") 

    
    def start_purchase(self):

        self.print_product_list()

        # 入力金額を判断する
        input_money = int(input("投入金額を入力してください "))
        while not(self.check_input_money(input_money)):
            input_money = int(input())
        
        # 商品が購入できるか確認する
        self.print_able_list()
        input_product = input("何を購入しますか(商品名/cancel)")
        while self.check_input_product(input_product):
            print(f"残金: {self.money}円")
            is_continue = input("続けて購入しますか(Y/N)")

            if is_continue == "N":
                break

            input_product = input("何を購入しますか(商品名/cancel)")
        
        # おつりの計算
        self.calc_change()
    
if __name__ == "__main__":
    vend_obj = vendculc()
    vend_obj.start_purchase()