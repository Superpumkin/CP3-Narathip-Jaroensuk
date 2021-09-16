from tkinter import *
import math

bmi = 0

def leftClickButton(event):
    bmi = float(textBox_Weight.get()) / math.pow(float(textBox_Height.get()) / 100 , 2)
    if bmi <= 18.5:
        bmi_Display = 'น้ำหนักน้อย / ผอม'
    elif bmi > 18.5 and bmi <= 22.90 :
        bmi_Display = 'ปกติ'
    elif bmi > 22.90 and bmi <= 24.90 :
        bmi_Display = 'เริ่มอ้วน / โรคอ้วนระดับ 1'
    elif bmi > 24.9 and bmi <= 29.90 :
        bmi_Display = 'อ้วน / โรคอ้วนระดับ 2'
    elif bmi > 29.90 :
        bmi_Display = 'อ้วนมาก / โรคอ้วนระดับ 3'
    label_calculate_2.configure(text = f'{bmi : .4f}')
    label_calculate.configure(text = bmi_Display)


main_window = Tk()
label_Height = Label(main_window , text = 'Height (cm.)')
label_Height.grid(row = 0 , column = 0)
textBox_Height = Entry(main_window)
textBox_Height.grid(row = 0 , column = 1)
label_Weight = Label(main_window , text = 'Weight (Kg.)')
label_Weight.grid(row = 1 , column = 0)
textBox_Weight = Entry(main_window)
textBox_Weight.grid(row = 1 , column = 1)
calculate_Button = Button(main_window , text = 'Calculate')
calculate_Button.bind('<Button-1>' , leftClickButton)
calculate_Button.grid(row = 2 , column = 0)
label_calculate = Label(main_window , text = '')
label_calculate.grid(row = 2 , column = 2)
label_calculate_2 = Label(main_window , text = '')
label_calculate_2.grid(row = 2 , column = 1)
main_window.mainloop()
