import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def generate_password():
    length = 16  # Set the password length
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure we have at least one of each type
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random choices from all pools combined
    all_characters = lowercase + uppercase + digits + special
    password_chars += [random.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle the characters to ensure randomness
    random.shuffle(password_chars)
    
    # Join the list into a string to form the final password
    password = ''.join(password_chars)
    
    # Display the password in the GUI entry
    password_entry.delete(0, tk.END)  # Clear any previous password
    password_entry.insert(0, password)

# Function to copy the password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()  # Clear the clipboard
        root.clipboard_append(password)  # Append the password to clipboard
        messagebox.showinfo("Copied", "Password copied to clipboard!")  # Confirm to user
    else:
        messagebox.showwarning("Warning", "No password generated to copy!")

# Set up the main window
root = tk.Tk()
root.title("Password Generator")

# Create a label
label = tk.Label(root, text="Generated Password:", font=("Helvetica", 12))
label.pack(pady=10)

# Create an entry widget to display the password
password_entry = tk.Entry(root, width=30, font=("Helvetica", 14), justify='center')
password_entry.pack(pady=10)

# Create a "Generate Password" button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12))
generate_button.pack(pady=10)

# Create a "Copy to Clipboard" button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Helvetica", 12))
copy_button.pack(pady=5)

# Run the main event loop
root.mainloop()
