def make_icecream(toppings):
    """ 列出製作冰淇淋的配料 """
    print("製作冰淇淋的配料如下：")
    for topping in toppings:
        print("--- ", topping)

# 定義製作飲料的函式
def make_drink(size, drink):
    """ 輸入飲料規格與種類，然後輸出飲料 """
    print("--- 客製化飲料 ---")
    print("尺寸：", size)
    print("飲料：", drink)