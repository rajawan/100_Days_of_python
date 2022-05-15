class Moneymachine:
    currency='$'
    COIN_VALUE = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
            }

    def __init__(self):
        self.profit=0
        self.money_received=0

    def report(self):
        print(f"Money {self.profit}")

    def process_coin(self):
        for coin in self.COIN_VALUE:
            self.money_received+=int(input(f"How many {coin}? "))
        return self.money_received

    def make_payment(self,cost):
        self.process_coin()
        if self.money_received>=cost:
            change=round(self.money_received-cost,2)
            print(f"Here is your return money {change}")
            self.profit+=cost
            self.money_received=0
            return True
        else:
            print(f"Sorry {self.money_received} is not enough money. Money Refunded ")
            self.money_received=0
            return False



new=Moneymachine()
print(new.process_coin())

    