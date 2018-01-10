import requests
base_url = 'https://api.fixer.io/latest?base=USD'
data = requests.get(base_url).json()
cad = data["rates"]["CAD"]
print("The latest exchange rate is 1 USD to " +str(cad)+ " CAD\n")


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
            xcFrom = float(input("Enter USD to exchange to CAD: $"))
            xcTo = xcFrom * cad
            print( str(round(xcFrom, 2)) + " USD is " + str(round(xcTo, 2)) + "CAD")
            break
        except ValueError:
            print("Please enter number only\n")

elif option == 2:
    while True:
        try:
            xcFrom = float(input("Enter CAD to exchange to USD: $"))
            xcTo = xcFrom / cad
            print( str(round(xcFrom, 2)) + " CAD is " + str(round(xcTo, 2)) + " USD")
            break
        except ValueError:
            print("Please enter number only\n")
