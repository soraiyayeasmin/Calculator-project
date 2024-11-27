import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            expression = str(result)
            display_var.set(expression)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            display_var.set("")
    elif text == "C":
        expression = ""
        display_var.set("")
    else:
        expression += text
        display_var.set(expression)

# Initialize the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""  # Holds the current expression
display_var = tk.StringVar()

# Display Screen
display = tk.Entry(root, textvar=display_var, font="Arial 20", bd=8, relief="ridge", justify="right")
display.pack(fill="x", padx=10, pady=10)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button Layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 0
col = 0

for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 15", width=5, height=2, relief="ridge", bg="lightgray")
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main event loop
root.mainloop()
