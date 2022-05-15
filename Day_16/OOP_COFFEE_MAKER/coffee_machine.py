class CoffeeMachine:
    def __init__(self):
        self.resources={
            'water':300,
            'milk':200,
            'coffee':100,
        }

    def report(self):
        for item in self.resources:
            print(f" {item} {self.resources[item]} ml")

    def is_item_avaliable(self,drink):
        for item in drink.resources:
            if drink.resources[item]>self.resources[item]:
                print(f"Sorry {item} not avaliable")
                return False
            return True

    def make_coffee(self,drink_name):
        for item in drink_name.resources:
            self.resources[item]-=drink_name[item]
        print(f"Here is your coffee {drink_name}")




    
new=CoffeeMachine()
new.report()