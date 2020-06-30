# imports
import bs4
import requests

# setup
result = requests.get("https://www.x-rates.com/table/?from=USD&amount=1")  # gets the data from the website

html_data = bs4.BeautifulSoup(result.text, "lxml")  # Beautiful soup
rates = html_data.select('.rtRates > a')  # Looked for the rates class which held the numbers

# stored the different rates to variables for each country
euro = rates[0].getText()
pound = rates[2].getText()
rupee = rates[4].getText()
aust_dollar = rates[6].getText()
cand_dollar = rates[8].getText()
sing_dollar = rates[10].getText()
swiss_franc = rates[12].getText()
may_ringgit = rates[14].getText()
jap_yen = rates[16].getText()
chin_yuan = rates[18].getText()

# Dictionary that links the word and the conversion rate number for it
country_rate = {'euro': euro, 'pound': pound, 'rupee': rupee, 'australian dollar': aust_dollar,
                'canadian dollar': cand_dollar, 'singapore dollar': sing_dollar, 'swiss franc': swiss_franc,
                'maylasion ringgit': may_ringgit, 'japanese yen': jap_yen, 'chinese yuan': chin_yuan}

# Placeholder
currency = 'abcd'

# main code runs now
print("\n\nYou can type Euro, Pound, Rupee, Australian dollar, Canadian dollar, Singapore dollar, Swiss franc,")
print("Maylasian ringgit, Japanese yen, Chinese yuan")

# Makes sure user gives valid input
while True:

    try:
        amount = int(input("\nAmount: "))

    except:
        print("Numbers only")

    else:
        break

while currency not in country_rate:
    currency = input("\nCurrency: ")
    currency = currency.lower()

    if currency not in country_rate:
        print("Please choose a country listed above")

# Stores the rates times the amount they gave in a variable
conversion_rate = float(country_rate.get(currency)) * amount

# Prints the results
print(f'\n{amount} dollars is equivalent to {round(conversion_rate, 2)} {currency.title()}s ')
print(f'{amount} ------> {round(conversion_rate, 2)}')
