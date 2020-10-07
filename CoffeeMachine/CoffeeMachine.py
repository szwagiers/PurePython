# main menu for coffee machine


def coffee_machine():
    print('')
    action = input('Write action (buy, fill, take, remaining, exit):')
    if action == 'buy':
        drink = input('''What do you want to buy? 1 - espresso, 2 - latter, 3 - cappuccino, bak - to main menu:''')
        making_coffee(drink)
    # service access
    elif action == 'fill':
        filling_machine()
    # check remaining ingredients
    elif action == 'remaining':
        remaining_resources()
    # take money from machine
    elif action == 'take':
        taking_money()
    elif action == 'exit':
        exit()

# check if there are enough ingredients


def check_available(water, milk, coffee):
    global water_available, milk_available, coffee_available, cups_available, money_in_machine
    if water_available - water <0:
        print('Sorry, not enough water')
    elif milk_available - milk <0:
        print('Sorry, not enough milk')
    elif coffee_available - coffee < 0:
        print('Sorry, not enough coffee')
    elif cups_available<=0:
        print('Sorry, not enough cups')
    else:
        return True
    coffee_machine()

# get ingredients, subtract them from containers and get back to main menu


def making_coffee(drink):
    global water_available, milk_available, coffee_available, cups_available, money_in_machine
    if drink == '1':
        if check_available(250, 50, 15):
            print('I have enough resources, making you a coffee!')
            water_available -= 250
            coffee_available -= 16
            cups_available -= 1
            money_in_machine += 4
    elif drink == '2':
        if check_available(350, 75, 20):
            print('I have enough resources, making you a coffee!')
            water_available -= 350
            milk_available -= 75
            coffee_available -= 20
            cups_available -= 1
            money_in_machine += 7
    elif drink == '3':
        if check_available(200, 100, 12):
            print('I have enough resources, making you a coffee!')
            water_available -= 200
            milk_available -= 100
            coffee_available -= 12
            cups_available -= 1
            money_in_machine += 6
    elif drink == 'back':
        coffee_machine()
    coffee_machine()

# filling machine with ingredients


def filling_machine():
    global water_available, milk_available, coffee_available, cups_available, money_in_machine
    adding_water = int(input('Write how many ml of water do you want to add:'))
    adding_milk = int(input('Write how many ml of milk do you want to add:'))
    adding_coffee = int(input('Write how many grams of coffee beans do you want to add:'))
    adding_cups = int(input('Write how many disposable cups of coffee do you want to add:'))

    water_available += adding_water
    milk_available += adding_milk
    coffee_available += adding_coffee
    cups_available += adding_cups
    coffee_machine()

# payment for coffee according to chosen type


def taking_money():
    global money_in_machine
    print(f'I gave you {money_in_machine}')
    money_in_machine -= money_in_machine
    coffee_machine()


# checking quantity of available ingredients

def remaining_resources():
    global water_available, milk_available, coffee_available, cups_available, money_in_machine
    print('')
    print('The coffee machine has:')
    print(f'{water_available} of water')
    print(f'{milk_available} of milk')
    print(f'{coffee_available} of coffee beans')
    print(f'{cups_available} of disposable cups')
    print(f'{money_in_machine} of money')
    coffee_machine()

# default values

water_available = 400
milk_available = 540
coffee_available = 120
cups_available = 9
money_in_machine = 550

# initiate coffee machine

coffee_machine()
