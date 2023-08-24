import os

from menu import MENU

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    global resources
    global profit
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def count_money():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_resourse(choice):
    

    check=MENU[choice]
    
    for item in resources:
        if resources[item] >=check["ingredients"][item]:
            return "True"
        else:
            return "False"
    
        


flag=True

while flag==True:
    
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    
    if choice=="report":
        os.system('cls||clear')
        report()

    elif choice=="off":
        flag=False

    elif not (choice=="report" and choice=="off"):
        varify=check_resourse(choice)
        if varify=="True":
            chose=MENU[choice]
            payment=count_money()
            cost=chose['cost']

            if cost>payment:
                os.system('cls||clear')
                print (f'your payment ${payment} is low it requires atleast ${cost}')

            elif cost <payment:

                exchange=payment-cost
                profit +=cost
                os.system('cls||clear')
                print (f'here is your exchange ${exchange}')
                print (f'here is your cofy enjoy')

                chose=MENU[choice]
                
                for item in resources:
                    resources[item] -=chose["ingredients"][item]
                

            else:
                os.system('cls||clear')
                print (f'here is your cofy enjoy')
                profit +=cost
                chose=MENU[choice]
                
                for item in resources:
                    resources[item] -=chose["ingredients"][item]
                
        elif varify=="False":
            os.system('cls||clear')
            print('resources are not sufficient')

    



        
        


        
        
    



























