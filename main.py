import requests
from tkinter import *
from tkinter import ttk
window = Tk()
from_country_var = StringVar(window)
to_country_var = StringVar(window)
amount_var = StringVar(window)

class CurrencyConverter:
    # to store conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # extracting rates from the json data
        self.rates = data["rates"]

    # function to do a simple cross multiplication between
    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR' :
            amount = amount/self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        # print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
        return amount

    # on change dropdown value
    def to_country_change_dropdown(*args):
        print(to_country_var.get())

    # on change dropdown value
    def from_country_change_dropdown(*args):
        print(from_country_var.get())


# Driver Code
if __name__ == "__main__":
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', 'dc9e577d2576a0cf01806038e64f0d63')
    c = CurrencyConverter(url)


    # GUI config
    window.title("Currency Converter")
    window.geometry('400x400')

    # Declaring Labels
    from_country_label = Label(window, text="From Country").grid(row=0, column=0)
    to_country_label = Label(window, text="To Country").grid(row=1, column=0)
    amount_label = Label(window, text="Amount").grid(row=2, column=0)

    country_choices1 = {"INR", "USD", "EUR", "AUD", "GBP", "CAD"}
    country_choices2 = {"INR", "USD", "EUR", "AUD", "GBP", "CAD"}
    # From and To countries dropdown
    from_country_menu = OptionMenu(window, from_country_var, *country_choices1).grid(row=0, column=1)
    from_country_var.trace('w', c.from_country_change_dropdown)

    to_country_menu = OptionMenu(window, to_country_var, *country_choices2).grid(row=1, column=1)
    to_country_var.trace('w', c.to_country_change_dropdown)

    amount_entry = Entry(window, textvariable=amount_var).grid(row=2, column=1)


    def submit():
        from_country = from_country_var.get()
        to_country = to_country_var.get()
        amount = int(amount_var.get())
        converted_amount = c.convert(from_country, to_country, amount)
        final_text = from_country + " : " + str(amount) + "\n" + to_country + " : " + str(converted_amount)
        converted_label = Label(window, text=final_text).grid(row=4, column=1)

    submit_button = Button(window, text="Convert", command=submit).grid(row=3, column=1)

    # c.convert(from_country,to_country, amount)
    window.mainloop()




