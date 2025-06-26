from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(5,6))]
    pass_numbers = [choice(numbers) for _ in range(randint(3,4))]
    pass_symbols = [choice(numbers) for _ in range(randint(3,4))]

    password_list = pass_letters + pass_numbers + pass_symbols
    shuffle(password_list)
    
    password = "".join(password_list)
    password_entry.delete(0, END) # Delete text
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def find_password():
    website = web_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Warning", message="Please fill the website's content!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo("No Data File Found!")
        else:
            try:
                web = data[website]
            except:
                messagebox.showinfo(title="Info",message="No details for the website exists!")
            else:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Your email: {email}\nYour password: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_entry.insert(0, "hoanggia.ng@samsung.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W)

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky=EW)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=EW)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

# Main loop
window.mainloop()