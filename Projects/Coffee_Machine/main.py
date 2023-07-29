water = 1000
milk = 800
coffee = 500
money_total = 0.00
money = 0.00


# this prints out a report of totals of coffee machine
def report():
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money_total}")

# function for coffees; has different amounts of ingredients and price
def latte():
    global money_total
    global water
    global milk
    global coffee
    global money
    if water >= 200:
        water -= 200

    else:
        print("We do not have enough water")

    if milk >= 200:
        milk -= 200

    else:
        print("We do not have enough milk")

    if coffee >= 100:
        coffee -= 100

    else:
        print("We do not have enough coffee")

    if money > 3:
        money_total += 3
        change = money - 3
        print("Here is your change: $" + str(format(change, ".2f")) + " and enjoy your latte! ")

    elif money == 3:
        money_total += 3
        change = money - 3
        print("Enjoy your latte!")

    else:
        print("You do not have enough money")


def cappuccino():
    global money_total
    global water
    global milk
    global coffee
    global money
    if water >= 200:
        water -= 200

    else:
        print("We do not have enough water")

    if milk >= 150:
        milk -= 150

    else:
        print("We do not have enough milk")

    if coffee >= 100:
        coffee -= 100

    else:
        print("We do not have enough coffee")

    if money > 2.5:
        money_total += 2.5
        change = money - 2.5
        print("Enjoy your latte!")
        print("Here is your change: $" + str(format(change, ".2f")) + " and enjoy your cappuccino! ")

    elif money == 2.5:
        money_total += 2.5
        change = money - 2.5
        print("Enjoy your cappuccino!")

    else:
        print("You do not have enough money")


def espresso():
    global money_total
    global water
    global milk
    global coffee
    global money
    if water >= 200:
        water -= 200

    else:
        print("We do not have enough water")

    if milk >= 100:
        milk -= 100

    else:
        print("We do not have enough milk")

    if coffee >= 100:
        coffee -= 100

    else:
        print("We do not have enough coffee")

    if money > 2:
        money_total += 2
        change = money - 2
        print("Enjoy your latte!")
        print("Here is your change: $" + str(format(change, ".2f")) + " and enjoy your espresso! ")

    elif money == 2:
        money_total += 2
        change = money - 2
        print("Enjoy your espresso!")

    else:
        print("You do not have enough money")


while 1 == 1:
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if option == "off":
        break
    if "report" == option:
        report()
    money = 0
    money += int(input("How many pennies?: ")) * 0.01
    money += int(input("How many nickels?: ")) * 0.05
    money += int(input("How many dimes?: ")) * 0.10
    money += int(input("How many quarters?: ")) * 0.25

    if option == "espresso":
        espresso()

    if option == "latte":
        latte()
    if option == "cappuccino":
        cappuccino()
