from tkinter import *
import math

# Standard variable
bmi = 0

# Function
def leftClickButton(event):
    bmi = float(textBox_Weight.get()) / math.pow(float(textBox_Height.get()) / 100 , 2)
    
    if bmi < 18.5:
        bmi_Display = 'ผอมเกินไป'
    elif bmi >= 18.6 and bmi <= 22.9 :
        bmi_Display = 'ปกติ'
    elif bmi > 23 and bmi <= 24.9 :
        bmi_Display = 'น้ำหนักเกิน'
    elif bmi > 25 and bmi <= 29.90 :
        bmi_Display = 'อ้วน'
    elif bmi > 30 :
        bmi_Display = 'อ้วนมาก'

    label_calculate_2.configure(text = f'{bmi : .4f}')
    label_calculate.configure(text = bmi_Display)


main_window = Tk()

# Height
label_Height = Label(main_window , text = 'Height (cm.)')
label_Height.grid(row = 0 , column = 0)
textBox_Height = Entry(main_window)
textBox_Height.grid(row = 0 , column = 1)

# Weight
label_Weight = Label(main_window , text = 'Weight (Kg.)')
label_Weight.grid(row = 1 , column = 0)
textBox_Weight = Entry(main_window)
textBox_Weight.grid(row = 1 , column = 1)

# Calculate Button
calculate_Button = Button(main_window , text = 'Calculate')
calculate_Button.bind('<Button-1>' , leftClickButton)
calculate_Button.grid(row = 2 , column = 0)
label_calculate = Label(main_window , text = '')
label_calculate.grid(row = 2 , column = 2)
label_calculate_2 = Label(main_window , text = '')
label_calculate_2.grid(row = 2 , column = 1)

# start
main_window.mainloop()
