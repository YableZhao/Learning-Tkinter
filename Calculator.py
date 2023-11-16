import tkinter as tk

root = tk.Tk()
root.title("Simple calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Global variables to store numbers and operations
numbers = []
operations = []

# Operation functions
def handle_operation(operation):
    current_number = entry.get()
    if current_number:
        numbers.append(int(current_number))
        operations.append(operation)
        entry.delete(0, tk.END)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number)),

def button_clear():
    entry.delete(0, tk.END),

def button_add():
    handle_operation("addition")

def button_subtract():
    handle_operation("subtraction")

def button_multiply():
    handle_operation("multiplication")
    
def button_divide():
    handle_operation("division")

def button_equal():
    numbers.append(int(entry.get()))
    entry.delete(0, tk.END)
    result = numbers[0]
    for i in range(len(operations)):
        if operations[i] == "addition":
            result += numbers[i + 1]
        elif operations[i] == "subtraction":
            result -= numbers[i + 1]
        elif operations[i] == "multiplication":
            result *= numbers[i + 1]
        elif operations[i] == "division":
            result /= numbers[i + 1]
    entry.insert(0, result)
    numbers.clear()
    operations.clear()

#buttons
button_width = 3
button_1 = tk.Button(root, text="1", padx=40, pady=20, width = button_width, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, width = button_width, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, width = button_width, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, width = button_width, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, width = button_width, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, width = button_width, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, width = button_width, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, width = button_width, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, width = button_width, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, width = button_width, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=40, pady=20, width = button_width, command=button_add)
button_subtract = tk.Button(root, text="-",padx=40, pady=20, width = button_width, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=40, pady=20, width = button_width, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=40, pady=20, width = button_width, command=button_divide)
button_equal = tk.Button(root, text="=", padx=40, pady=20, width = button_width, command=button_equal)
button_clear = tk.Button(root, text="C", padx=40, pady=20, width = button_width, command=button_clear)

# Display buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=6, column=0)
button_5.grid(row=6, column=1)
button_6.grid(row=6, column=2)
button_7.grid(row=9, column=0)
button_8.grid(row=9, column=1)
button_9.grid(row=9, column=2)
button_0.grid(row=12, column=0)

button_add.grid(row=3, column=3)
button_subtract.grid(row=6, column = 3)
button_multiply.grid(row=9, column = 3)
button_divide.grid(row=12, column = 3)
button_clear.grid(row=12, column=1)
button_equal.grid(row=12, column=2)


root.mainloop()

