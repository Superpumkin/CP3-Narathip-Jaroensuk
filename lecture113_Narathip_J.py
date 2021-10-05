import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from forex_python.converter import CurrencyRates

current = CurrencyRates()
convert = 0

def leftclickToConvert(event) :
    convert = float(boxSelected.get()) * current.get_rate(currentInput.get() , currentDisplay.get())
    l_amountChange.configure(text = f'{convert:.3f}')



main = tk.Tk()
main.geometry('500x200')
main.title('CurrencyRates')
main.configure(background= '#C0C0C0')

currentSelected = tk.Label(main , text='CurrentSelect' ,
                            background='blue' , foreground= 'white' ,
                            font = ('Helvetica' , 22 , 'bold'))

currentSelected.grid(row= 0 , column= 0)

currentInput = ttk.Combobox(main , width= 20 ,
                                values= (
                                    "USD",
                                    "JPY",
                                    "EUR",
                                    "THB",
                                    "IDR",
                                    "ILS",
                                    "AUD",
                                    "HKD"
                                ))
currentInput.grid(row= 0 , column = 1)

currentDisplay = tk.Label(main , text='CurrentChange' ,
                            background='red' , foreground= 'white' ,
                            font = ('Helvetica' , 20 , 'bold'))

currentDisplay.grid(row= 1 , column= 0)

currentDisplay = ttk.Combobox(main , width= 20 ,
                                values= (
                                    "USD",
                                    "JPY",
                                    "EUR",
                                    "THB",
                                    "IDR",
                                    "ILS",
                                    "AUD",
                                    "HKD"
                                ))
currentDisplay.grid(row= 1 , column = 1)

amountInput = tk.Label(main , text= 'Enter Amount' ,
                        background='blue' , foreground= 'white' ,
                        font = ('Helvetica' , 20 , 'bold'))
amountInput.grid(row= 4 , column= 0)

boxSelected = tk.Entry(main , width= 20)
boxSelected.grid(row= 4 , column= 1)

amountChange = tk.Label(main , text= 'Amount to Change' ,
                        background='red' , foreground= 'white' ,
                        font = ('Helvetica' , 20 , 'bold'))
amountChange.grid(row= 6 , column= 0)

l_amountChange = tk.Label(main , text= '0')
l_amountChange.grid(row= 6 , column= 1)

convertButton = tk.Button(main , text='Convert',
                            width= 7 , height= 1)
convertButton.bind('<Button-1>',leftclickToConvert)
convertButton.grid(row= 8 , column= 1)



main.mainloop()
