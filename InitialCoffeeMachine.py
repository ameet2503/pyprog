d_water = 400
d_milk = 540
d_coffee = 120
d_cups = 9
d_money = 550


def status(d_water, d_milk, d_coffee, d_cups, d_money):
    print("The coffee machine has:")
    print(d_water, " of water")
    print(d_milk, " of milk")
    print(d_coffee, " of coffee beans")
    print(d_cups, " of disposable cups")
    print(d_money, " of money")


def expr_calc():
    global d_water
    global d_coffee
    global d_cups
    global d_money
    if (d_water >= 250) and (d_coffee >= 16) and (d_cups >= 1):
        print("I have enough resources, making you a coffee!")
        d_water = d_water - 250
        d_coffee = d_coffee - 16
        d_cups = d_cups - 1
        d_money = d_money + 4
    else:
        print("Sorry, not enough water!")


def latte_calc():
    global d_water
    global d_milk
    global d_coffee
    global d_cups
    global d_money
    if (d_water >= 350) and (d_milk >= 75) and (d_coffee >= 20) and (d_cups >= 1):
        print("I have enough resources, making you a coffee!")
        d_water = d_water - 350
        d_milk = d_milk - 75
        d_coffee = d_coffee - 20
        d_cups = d_cups - 1
        d_money = d_money + 7
    else:
        print("Sorry, not enough water!")


def cappuccino_calc():
    global d_water
    global d_milk
    global d_coffee
    global d_cups
    global d_money
    if (d_water >= 200) and (d_milk >= 100) and (d_coffee >= 12) and (d_cups >= 1):
        print("I have enough resources, making you a coffee!")
        d_water = d_water - 200
        d_milk = d_milk - 100
        d_coffee = d_coffee - 12
        d_cups = d_cups - 1
        d_money = d_money + 6
    else:
        print("Sorry, not enough water!")


def add_ingredients():
    global d_water
    global d_milk
    global d_coffee
    global d_cups
    global d_money
    water_input = int(input("Write how many ml of water do you want to add: > "))
    milk_input = int(input("Write how many ml of milk do you want to add: > "))
    coffee_input = int(input("Write how many grams of coffee beans do you want to add: > "))
    coffee_cups = int(input("Write how many disposable cups of coffee do you want to add: > "))
    d_water = int(d_water) + water_input
    d_milk = int(d_milk) + milk_input
    d_coffee = int(d_coffee) + coffee_input
    d_cups = int(d_cups) + coffee_cups


def take_money():
    global d_money
    #    money = input("I gave you $")
    print("I gave you $", +d_money)
    d_money = d_money - d_money


def buy_coffee():
    user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: > ")
    if user_input == '1':
        expr_calc()
    elif user_input == '2':
        latte_calc()
    elif user_input == '3':
        cappuccino_calc()
    else:
        count = False


count = True
while True:
    action = input("Write action (buy, fill, take, remaining, exit): > ")
    # status(d_water, d_milk, d_coffee, d_cups, d_money)
    if action == "buy":
        buy_coffee()
    elif action == "fill":
        add_ingredients()
    elif action == "take":
        take_money()
    elif action == "remaining":
        status(d_water, d_milk, d_coffee, d_cups, d_money)
    else:
        break


