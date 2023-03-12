import tkinter as tk


def set_fullname():
    print("Button clicked")
    f_name = firstEntry.get()
    s_name = surnameEntry.get()
    #  fullNameEntry.insert(0, f_name + " " + s_name)
    fullNameEntry.insert(0, f_name + " " + s_name)


form = tk.Tk()

form.title("My python Form")

fullStringVar = tk.StringVar()

firstLabel = tk.Label(form, text="First Name:")
firstEntry = tk.Entry(form)

surnameLabel = tk.Label(form, text="Surname:")
surnameEntry = tk.Entry(form, relief="raised")

fullNameLabel = tk.Label(form, text="Full Name:")
#  fullNameEntry = tk.Entry(form)
fullNameEntry = tk.Entry(form, textvariable=fullStringVar)

btnFullName = tk.Button(form, text="Full Name", command=set_fullname)

firstLabel.grid(row=0, column=0, padx=15, pady=15)
firstEntry.grid(row=0, column=1, padx=15, pady=15)

surnameLabel.grid(row=1, column=0, padx=15, pady=15)
surnameEntry.grid(row=1, column=1, padx=15, pady=15)

fullNameLabel.grid(row=2, column=0, padx=15, pady=15)
fullNameEntry.grid(row=2, column=1, padx=15, pady=15)

btnFullName.grid(columnspan=2, padx=15, pady=15)

form.mainloop()  # for the form to stay on the screen and not disappear
