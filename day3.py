import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Retrieve values from the entry fields
    name = entry_name.get()
    email = entry_email.get()

    # Display a message with the form data
    message = f"Name: {name}\nEmail: {email}"
    messagebox.showinfo("Form Submission", message)

# Create the main window
root = tk.Tk()
root.title("Simple Form")

# Create and place form elements
label_name = tk.Label(root, text="Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Run the Tkinter event loop
root.mainloop()
