from pass_check_helper import checkPass
import tkinter as tk
from tkinter import Radiobutton, messagebox


def checkPressed(win, qe, password, flag):
    qe.delete(0, tk.END)
    # print('Pass= ', password, 'flag= ', flag)
    response = checkPass(password=password, flag=flag)
    messagebox.showinfo('Result',
                        response)


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x400")
greeting_label = tk.Label(
    root, text="Enter the Password Below: ", font=10)
greeting_label.place(x=10, y=50)

query_entry = tk.Entry(root, font=10)
query_entry.place(x=50, y=100)
flag = tk.IntVar()
r1 = Radiobutton(root, text='Shallow Check', variable=flag, value=0, font=10)
r1.place(x=50, y=150)
r2 = Radiobutton(root, text='Deep Check', variable=flag, value=1, font=10)
r2.place(x=50, y=190)
r3 = Radiobutton(root, text='Full Check', variable=flag, value=2, font=10)
r3.place(x=50, y=230)

query_button = tk.Button(
    root, text="Check", font=10, command=lambda: checkPressed(win=root,
                                                              password=query_entry.get(),
                                                              qe=query_entry, flag=flag.get()))
query_button.place(x=120, y=290)

root.mainloop()
