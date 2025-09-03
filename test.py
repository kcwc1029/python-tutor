# ch15_20.py
class Banks():
    title = 'Taipei Bank'

    def __init__(self, uname, money):
        self.name = uname
        self.balance = money

    def save_money(self, money):
        # 斷言：存款金額必須大於 0
        assert money > 0, "存款金額必須為正數"
        self.balance += money
        print("存款", money, "完成")

    def withdraw_money(self, money):
        # 斷言：提款金額必須小於或等於目前餘額
        assert money <= self.balance, "存款餘額不足，無法提款"
        self.balance -= money
        print("提款", money, "完成")

    def get_balance(self):
        print(self.name.title(), "目前餘額:", self.balance)

# --- 程式執行 ---
hungbank = Banks('Hung', 100)
hungbank.get_balance()
hungbank.save_money(400)      # 存款 400 (教材此處為500，為與圖片結果一致改為400)
hungbank.get_balance()
hungbank.withdraw_money(700)  # 試圖提款 700
hungbank.get_balance()