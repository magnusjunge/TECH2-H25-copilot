

def generate_password(lenght = 8):
    import random
    import string

    if lenght < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character sets
    # Restrict string.punctuation to the required subset so the password includes at least one of them
    special_char = "!@#$%^&*()-_=+`"
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_char)
    ]
    # Ensure the first character is not a digit or special character
    
    # Fill the rest of the password length with a mix of all character sets
    all_characters = lowercase + uppercase + digits + special_char 
    password += random.choices(all_characters, k=lenght - 5)

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)
    first_char = random.choice(lowercase + uppercase)
    password.insert(0, first_char)

    return ''.join(password)

def create_gui():
    import tkinter as tk
    from tkinter import ttk, messagebox

    def generate():
        try:
            length = int(length_var.get())
            if 8 <= length <= 16:
                password = generate_password(length)
                password_var.set(password)
            else:
                messagebox.showerror("Error", "Length must be between 8 and 16 characters.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def copy_to_clipboard():
        if password_var.get():
            root.clipboard_clear()
            root.clipboard_append(password_var.get())
            messagebox.showinfo("Success", "Password copied to clipboard!")

    # Create the main window
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x250")
    root.resizable(False, False)

    # Style configuration
    style = ttk.Style()
    style.configure('TButton', padding=5)
    style.configure('TLabel', font=('Helvetica', 10))
    style.configure('TEntry', padding=5)

    # Create and pack widgets
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Length input
    length_label = ttk.Label(main_frame, text="Password Length (8-16):")
    length_label.pack(pady=5)
    
    length_var = tk.StringVar(value="8")
    length_entry = ttk.Entry(main_frame, textvariable=length_var, width=10, justify='center')
    length_entry.pack(pady=5)

    # Generate button
    generate_button = ttk.Button(main_frame, text="Generate Password", command=generate)
    generate_button.pack(pady=10)

    # Password display
    password_var = tk.StringVar()
    password_entry = ttk.Entry(main_frame, textvariable=password_var, width=30, justify='center')
    password_entry.pack(pady=10)

    # Copy button
    copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=copy_to_clipboard)
    copy_button.pack(pady=5)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()  
