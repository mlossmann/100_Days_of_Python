def add(*args):
    # ans = 0
    # for n in args:
    #     ans += n
    # return ans
    print(args)

print(add(10,10,10,20))


# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     return(n)
#
# print(calculate(2, add=3, multiply=5))

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(make="Tesla")
print(my_car.make)


from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
my_label['text'] = "LOOK MA, New Text!"
my_label.config(text="Even more new text!")


# Button


def button_clicked():
    my_label['text'] = input.get()


button = Button(text="Click Me!", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.insert(END, string="Hello!")
input.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
