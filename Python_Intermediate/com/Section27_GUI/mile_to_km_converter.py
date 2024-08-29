from tkinter import *

# creating a function for miles to milometer


def mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.minsize(500, 300)
window.title("mile to km converter")

miles_input = Entry()
miles_input.grid(column=1, row=0)


miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calcualte_button = Button(text="calculate", command=mile_to_km)
calcualte_button.grid(column=1, row=2)

mainloop()
