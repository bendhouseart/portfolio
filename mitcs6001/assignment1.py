#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:30:32 2017

@author: anthony
"""

# total_cost = the cost of your dream house
# portion_down_payment = the percentage of total cost you want to 
# pay down on your house
# current_savings is the current amount of savings you possess
# r is the return on investment you are currently receiving on your
# current_savings
# annual_salary = your annual pay
# portion_saved = the ammount of your salary each month that you are 
# applying toworads your house savings.
# monthly_salary is annual_salary/12

# this program calculates how many months it will take you to save up
# enough money for a down payment. Your program will calculate this by 
# receiving input from the user in the form of raw input for the variables
# starting annual salary (annual_salary), the portion of your salary to be
# saved (portion_saved), and the cost of your dream home (total_cost)

#float total_cost, portion_down_payment = 0.25, r, current_savings, annual_salary, portion_saved, monthly_salary

# you make the assumption that your investments make a return of 0.04 annually
r = 0.04

current_savings = 0.0


print("Hiya welcome to the handy dandy home down payment calculator!")
print("Let's not waste any time and get started right away.")
annual_salary = float(input("What's your current or projected annual salary?"))
print("")
portion_saved = float(input("What percentage of your current salary would you like to save each month?"))
print("")
total_cost = float(input("What is the purchase price of the home you are dreaming of?"))

monthly_salary = annual_salary/12.0
month = 0
portion_down_payment = 0.25*total_cost
while current_savings < portion_down_payment:
    month += 1 
    current_savings = current_savings + current_savings*r/12.0 + (portion_saved*monthly_salary) 
    print(month,current_savings)
print("You will be bale to make a $", portion_down_payment, " on you house in ", month, " months.")