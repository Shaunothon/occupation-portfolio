from tkinter import*    
import tkinter.messagebox

#GUI
ccApp = tkinter.Tk()
ccApp.title("UNLV PROJECT")
ccApp.configure(bg="green")
ccApp.geometry('1100x700')
ccApp.configure(background = 'green')
win_dimension = Frame(ccApp, bg = 'white', pady = 3, width = 1300, height = 1000)
win_dimension.grid(row = 0, column = 0)
win_dimension.configure(bg="green")
header = tkinter.Label(win_dimension,text = "CURRENCY CONVERTOR", font =("Times New Roman", 50, 'bold'), 
bg = 'green', fg = 'white')

header.grid(column = 1, row = 0)

# variable for from currency
varOne = tkinter.StringVar(ccApp)
# variable for to currency 
varTwo = tkinter.StringVar(ccApp)

# default value for variable
varOne.set("currency")
varTwo.set("currency")
varThree = tkinter.StringVar(ccApp)

#---------------------FUNCTIONS-----------------------------------
 
def currency_conversion():
    """ to convert an amount given from a currency to another currency"""
    from  forex_python.converter import CurrencyRates
    cr = CurrencyRates() 

    # value selected for from and to
    startC = varOne.get()
    endC = varTwo.get()

    if curr_box_from.get() == "":
        tkinter.messagebox.showinfo("Error", "No value was entered\n Please enter a numerical value")
    elif (curr_box_from.get().isdigit() == False):
        tkinter.messagebox.showinfo("Error", "Incorrect value.\n Please enter a positive numerical value.")
    elif (startC == "currency" or endC == "currency"):
        tkinter.messagebox.showinfo("Error !!",
        "One or more currency codes was not selected\n Please select a currency code from drop down menu.")
    else:
        curr_box_val = float(curr_box_from.get()) #cast string to float
        converted_amount = cr.convert(startC, endC, curr_box_val) #conversion
        curr_box_conv.delete(0, tkinter.END) #delete current data in field
        curr_box_conv.insert(0, str(converted_amount)) #populates new data  

    #symbol retrieval
    curr_symbol(startC, endC)

def clear():
    """ to reset all fields to empty or default"""
    #zero out entry fields
    curr_box_from.delete(0,tkinter.END)
    curr_box_conv.delete(0,tkinter.END)
    from_sym.delete(0, tkinter.END)
    to_sym.delete(0, tkinter.END)
    cfound.delete(0,tkinter.END)
    cName.delete(0,tkinter.END)

    #default scroll down menu
    varOne.set("currency")
    varTwo.set("currency")
    varThree.set(" ")

def curr_symbol(value_one, value_two):
    """ to produce a currency symbol sign to and from"""
    from forex_python.converter import CurrencyCodes
    cc = CurrencyCodes()
    #from symbol
    from_sym.delete(0, tkinter.END)
    from_sym.insert(0,cc.get_symbol(value_one))
    #to symbol
    to_sym.delete(0, tkinter.END)
    to_sym.insert(0,cc.get_symbol(value_two))
    

def findCurrency():
    from forex_python.converter import CurrencyCodes
    """ to find the currency type of a country"""
    cc = CurrencyCodes()
    findC = varThree.get()
    if findC == "" or findC == " ":
       tkinter.messagebox.showinfo("Error", 
       "A country was not selected\n Please select a country from drop down menu.") 
    cfound.delete(0, tkinter.END)
    cfound.insert(0,currency_dict[findC])
    cName.delete(0,tkinter.END)
    cName.insert(0,cc.get_currency_name(currency_dict[findC]))
 
#----------------------------------- FIELD LABELS------------------------------
#---------------Enter a Value: 
valText = tkinter.Label(ccApp,  text = "\tEnter a value: ", font =("Times New Roman", 30, 'bold'), 
bg = 'green', fg = 'white')

valText.grid(row = 2, column = 0)
#---------------From (currency):
fromText = tkinter.Label(ccApp,  text = "\tFrom (currency): ", font =("Times New Roman", 30, 'bold'), 
bg = 'green', fg = 'white'
)

fromText.grid(row = 3, column = 0)
#---------------To (currency):
toText = tkinter.Label(ccApp,  text = "\tTo (currency): ", font =("Times New Roman", 30, 'bold'), 
bg = 'green', fg = 'white'
)

toText.grid(row = 4, column = 0)
#---------------Converted Value:
convText = tkinter.Label(ccApp,  text = "\tConverted Amount: ", font =("Times New Roman", 30, 'bold'), 
bg = 'green', fg = 'white')

convText.grid(row = 9, column = 0)

#----------------Find a currency:
find_a_curr = tkinter.Label(ccApp, text = "\tDon't know which currency you need?\n Select a country: ", 
font =("Times New Roman", 30, 'bold'), bg = 'green', fg = 'white')

find_a_curr.grid(row = 12, column = 0)

#---------------Filler space:
filler = tkinter.Label (ccApp,  text = "", font =("Times New Roman", 30, 'bold'), 
bg = 'green', fg = 'black')

filler.grid(row = 6, column = 1)

filler = tkinter.Label (ccApp,  text = "", font =("Times New Roman", 30, 'bold'), 
bg = 'green', fg = 'black')

filler.grid(row = 8, column = 1)

filler = tkinter.Label (ccApp,  text = "", font =("Times New Roman", 30, 'bold'), 
bg = 'green', fg = 'black')

filler.grid(row = 10, column = 1)

filler = tkinter.Label (ccApp,  text = "", font =("Times New Roman", 30, 'bold'), 
bg = 'green', fg = 'black')

filler.grid(row = 15, column = 2)

#-------currency list
currency_names = ['USD', "EUR", "GBP", "ILS", "DKK", "CAD", "IDR", "BGN",
    "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", 
    "CNY", "TRY", "HRK", "NZD", "THB", "LTL", "NOK", "RUB",
    "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]
#--------country list
country_list = ["Canada","Indonesia","Bulgaria","Japan",
    "Hungary","Romania","Malaysia","Sweden","Singapore","Hong Kong","Australia",
    "Switzerland", "South Korea","China","Turkey","Croatia","New Zealand","Thailand", 
    "Lithuania","Norway","Russia","India","Mexico","Czech Republic","Brazil","Poland",
    "Philippines","South Africa"]
#--------dictionary
currency_dict = {
'United States': 'USD',
'Eurozone': 'EUR',
'United Kingdom': 'GBP',
'Israel': 'ILS',
'Denmark': 'DKK',
'Canada': 'CAD',
'Indonesia': 'IDR',
'Bulgaria': 'BGN',
'Japan': 'JPY',
'Hungary': 'HUF',
'Romania': 'RON',
'Malaysia': 'MYR',
'Sweden': 'SEK',
'Singapore': 'SGD',
'Hong Kong': 'HKD',
'Australia': 'AUD',
'Switzerland': 'CHF',
'South Korea': 'KRW',
'China': 'CNY',
'Turkey': 'TRY',
'Croatia': 'HRK',
'New Zealand': 'NZD',
'Thailand': 'THB',
'Lithuania': 'LTL',
'Norway': 'NOK',
'Russia': 'RUB',
'India': 'INR',
'Mexico': 'MXN',
'Czech Republic': 'CZK',
'Brazil': 'BRL',
'Poland': 'PLN',
'Philippines': 'PHP',
'South Africa': 'ZAR'
}

#-------------------------------FIELDS---------------------
#-------field to enter currency
curr_box_from = tkinter.Entry(ccApp)
curr_box_from.grid(row = 2, column = 1)

#-------field to populate conversion
curr_box_conv = tkinter.Entry(ccApp)
curr_box_conv.grid(row = 9, column = 1)

#-------field to populate from currency symbol
from_sym = tkinter.Entry(ccApp)
from_sym.grid(row = 2, column = 2)
#-------field to populate to currency symbol
to_sym = tkinter.Entry(ccApp)
to_sym.grid(row = 9, column = 2)
#-------field to populate to currency found
cfound = tkinter.Entry(ccApp)
cfound.grid(row = 12, column = 2)
#-------field to populate to currency name
cName = tkinter.Entry(ccApp)
cName.grid(row = 13, column = 2)
#scrolldown currency menu
#-------from menu
b_list = tkinter.OptionMenu(ccApp, varOne, *currency_names)
b_list.grid(row = 3, column = 1)
#-------to menu
c_list = tkinter.OptionMenu(ccApp, varTwo, *currency_names )
c_list.grid(row = 4, column = 1)
#scrolldown country menu
#-------from menu
keys = currency_dict.keys()
values = currency_dict.values()
cMenu= tkinter.OptionMenu(ccApp, varThree, *country_list)
cMenu.grid(row = 12, column = 1)


#----------Buttons
convert_Button =  Button(ccApp, font = ("Times New Roman", 30, 'bold'), text = "CALCULATE", 
bg = 'red', fg = 'red', command = currency_conversion)
convert_Button.grid(row = 7, column = 0)

clear_Button = Button(ccApp, font = ("Times New Roman", 30, 'bold'), text = "CLEAR DATA", 
bg = 'red', fg = 'red', command = clear)
clear_Button.grid(row = 16, column = 2)

find_currency_Button = Button(ccApp, font = ("Times New Roman", 30, 'bold'), text = "FIND CURRENCY", 
bg = 'red', fg = 'red', command = findCurrency)
find_currency_Button.grid(row = 13, column = 0)



ccApp.mainloop()

