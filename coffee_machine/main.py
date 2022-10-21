#!/usr/bin/env python3
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_status = 'on'
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_status != 'off':
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        machine_status = choice
        print(f"Profits: ${money_machine.profit}")
    else:
        drink = menu.find_drink(choice)
        if drink != None:
            if not coffee_maker.is_resource_sufficient(drink):
                continue
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)