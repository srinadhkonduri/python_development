from tkinter import *
window = Tk()
window.title("my first gui program")
window.minsize(500, 300)

# label
my_label = Label(text="i am a label", font=("arial", 24, "bold"))
# here this pack keyword is very useful for showing the output for the display
my_label.pack()
# here's the main code of which helps to keep the screen turn on

# button


def button_clicked():
    print("i got clicked")
    # my_label.config(text="button got clicked")
    new_text = message.get()
    message.config(text=new_text)


button = Button(text="click me", command=button_clicked)
button.pack()


# input giivng
message = Entry(width=10)
message.pack()
print(message.get())

mainloop()
