from tkinter import *
import time
# setting window
window = Tk()
window.minsize(width=300, height=100)
window.title("My First GUI Program")
# #
# # Label
# my_label = Label(text="Hiii", font=("Arial", 24, "bold"))
# my_label.pack()
# #
# # Using button
# def button_function():
#     my_label.config(text=f"{input.get()}")
#
#
# button = Button(text="Click me", command=button_function)
# button.pack()
# #
# # using Entry
# input = Entry(width=10)
# input.pack()
label1 = Label(text="is equal to", font=("Arial", 24, ))
label1.grid(row=1, column=0)

label2 = Label(text="Miles", font=("Arial", 24, "bold"))
label2.grid(row=0, column=2)

label3 = Label(text="Km", font=("Arial", 24, "bold"))
label3.grid(row=1, column=2)

label4 = Label(text="0", font=("Arial", 24, ))
label4.grid(row=1, column=1)

input = Entry(width=15, font=("Arial", 24, "bold"))
input.grid(row=0, column=1)


def buttonFunction():
    label4.config(text=f"{round(int(input.get())*1.609344)}")


button = Button(text="Calculate", width=10, command=buttonFunction, font=("Arial", 24, "bold"))
button.grid(row=2, column=1)




window.mainloop()