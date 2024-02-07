import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()

    message = f"Name: {name}\nEmail: {email}"
    messagebox.showinfo("Form Submission", message)

root = tk.Tk()
root.title("Simple Form")

label_name = tk.Label(root, text="First Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_name = tk.Label(root, text="Middle Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_name = tk.Label(root, text="Last Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Age:")
label_age.pack()

entry_age = tk.Entry(root)
entry_age.pack()

label_number = tk.Label(root, text="phone number:")
label_number.pack()

entry_number = tk.Entry(root)
entry_number.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()



submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()
