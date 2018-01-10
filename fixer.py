# Created by Scott Kim
# Lab1 Part 4
# This program will retreive the latest USD to CAD exchange rate and user will be able to exchange either from USD to CAD or CAD to USD

import requests
import sys


base_url = 'https://api.fixer.io/latest?base=USD'
# http://www.hashbangcode.com/blog/stopping-code-execution-python request exception
try:
    data = requests.get(base_url).json()
    cad = data["rates"]["CAD"]
    print("The latest exchange rate is 1 USD to " +str(cad)+ " CAD\n")
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit()


while True:
    try:
        option = int(input("Please select an option\n"+
        "1. USD to CAD\n"+
        "2. CAD to USD\n"))
        if option != (1 or 2):
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid number\n")

if option == 1:
    while True:
        try:
            xcFrom = float(input("\nEnter USD to exchange to CAD: $"))
            xcTo = xcFrom * cad
            print( str(round(xcFrom, 2)) + " USD is " + str(round(xcTo, 2)) + "CAD")
            break
        except ValueError:
            print("Please enter number only")

elif option == 2:
    while True:
        try:
            xcFrom = float(input("\nEnter CAD to exchange to USD: $"))
            xcTo = xcFrom / cad
            print( str(round(xcFrom, 2)) + " CAD is " + str(round(xcTo, 2)) + " USD")
            break
        except ValueError:
            print("Please enter number only")
