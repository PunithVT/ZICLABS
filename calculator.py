from tkinter import *

# globally declare the expression variable
expression = ""

# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into a string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by an empty string
        expression = ""

    # if an error is generated then handle
    # by the except block
    except:

        equation.set(" Error ")
        expression = ""

# Function to clear the contents
# of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# create a GUI window
gui = Tk()

# set the background color of the GUI window
gui.configure(background="#282c34")  # Dark background color

# set the title of the GUI window
gui.title("Awesome Calculator")

# set the configuration of GUI window
window_width = 320
window_height = 480
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - window_height) / 2)
gui.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Set custom font
font_style = ("Helvetica", 16)

# StringVar() is the variable class
# we create an instance of this class
equation = StringVar()

# create the text entry box for
# showing the expression.
expression_field = Entry(gui, textvariable=equation, font=font_style, bd=10, insertwidth=4, width=14, justify='right')
expression_field.grid(row=0, column=0, columnspan=4)

# create Buttons and place them at a particular
# location inside the root window.
# when the user presses the button, the command or
# function affiliated with that button is executed.
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    Button(gui, text=button, fg='white', bg='#61dafb', font=font_style,
           command=lambda b=button: press(b) if b != '=' else equalpress(), height=2, width=5).grid(row=row_val, column=col_val, pady=5, padx=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# start the GUI
gui.mainloop()


