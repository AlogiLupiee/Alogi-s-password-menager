from tkinter import *
import webbrowser

def submit():
    with open('passlist.txt', 'a') as File:
        passstr = entrypass.get()
        namestr = entryname.get()
        File.write('\n')
        File.write(namestr)
        File.write(" ")
        File.write(passstr)

tk = Tk()
tk.title("Alogi's password menager 1.0")
tk.config(padx=50, pady=50)

labelname = Label(tk, text = "Name/Mail:").grid(column = 1, row = 1)

entryname = Entry(tk)
entryname.grid(column = 2, row = 1)

labelpass = Label(tk, text = "Password:").grid(column = 1, row = 2)

entrypass = Entry(tk)
entrypass.grid(column = 2, row = 2)

submitbttn = Button(tk, text = "Submit", activebackground = "red", command = submit).grid(column = 2, row = 3)

menu = Menu(tk)
tk.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "Menu", menu = filemenu)
filemenu.add_command(label = 'Exit', command = tk.quit)
filemenu.add_command(label = 'About me', command = lambda: webbrowser.open_new('https://github.com/AlogiLupiee'))

mainloop()