class CoffeeMachine:

    def __init__(self):
        self.g_water = 400
        self.g_milk = 540
        self.g_coffee = 120
        self.g_cups = 9
        self.g_money = 550
        self.count = None

    def status(self):
        print("The coffee machine has:")
        print(self.g_water, " of water")
        print(self.g_milk, " of milk")
        print(self.g_coffee, " of coffee beans")
        print(self.g_cups, " of disposable cups")
        print(self.g_money, " of money")

    def takemoney(self):
        d_money = self.g_money
        #    money = input("I gave you $")
        print("I gave you $", +d_money)
        self.g_money = self.g_money - d_money

    def add_ingredients(self):
        water_input = int(input("Write how many ml of water do you want to add: > "))
        milk_input = int(input("Write how many ml of milk do you want to add: > "))
        coffee_input = int(input("Write how many grams of coffee beans do you want to add: > "))
        coffee_cups = int(input("Write how many disposable cups of coffee do you want to add: > "))
        self.g_water = int(self.g_water) + water_input
        self.g_milk = int(self.g_milk) + milk_input
        self.g_coffee = int(self.g_coffee) + coffee_input
        self.g_cups = int(self.g_cups) + coffee_cups

    def expr_calc(self):

        if (self.g_water >= 250) and (self.g_coffee >= 16) and (self.g_cups >= 1):
            print("I have enough resources, making you a coffee!")
            self.g_water = self.g_water - 250
            self.g_coffee = self.g_coffee - 16
            self.g_cups = self.g_cups - 1
            self.g_money = self.g_money + 4
        else:
            print("Sorry, not enough water!")

    def latte_calc(self):
        if (self.g_water >= 350) and (self.g_milk >= 75) and (self.g_coffee >= 20) and (self.g_cups >= 1):
            print("I have enough resources, making you a coffee!")
            self.g_water = self.g_water - 350
            self.g_milk = self.g_milk - 75
            self.g_coffee = self.g_coffee - 20
            self.g_cups = self.g_cups - 1
            self.g_money = self.g_money + 7
        else:
            print("Sorry, not enough water!")

    def cappuccino_calc(self):
        if (self.g_water >= 200) and (self.g_milk >= 100) and (self.g_coffee >= 12) and (self.g_cups >= 1):
            print("I have enough resources, making you a coffee!")
            self.g_water = self.g_water - 200
            self.g_milk = self.g_milk - 100
            self.g_coffee = self.g_coffee - 12
            self.g_cups = self.g_cups - 1
            self.g_money = self.g_money + 6
        else:
            print("Sorry, not enough water!")

    def buy_coffee(self):
        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: > ")
        if user_input == '1':
            act.expr_calc()
        elif user_input == '2':
            act.latte_calc()
        elif user_input == '3':
            act.cappuccino_calc()
        else:
            self.count = False


act = CoffeeMachine()
count = True
while True:
    action = input("Write action (buy, fill, take, remaining, exit): > ")
    print(action)
    if action == "buy":
        act.buy_coffee()
    elif action == "fill":
        act.add_ingredients()
    elif action == "take":
        act.takemoney()
    elif action == "remaining":
        act.status()
    else:
        break
