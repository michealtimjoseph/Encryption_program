from tkinter import *
from tkinter import filedialog
from tkinter import ttk  # For Progressbar

# Initialize main window
base = Tk()
base.title("Encrypt and Decrypt Program")
base.geometry('450x350')
base.configure(bg='gray')
base.resizable(False, False)

# Create frames for screens
welcome_frame = Frame(base, bg='gray')
main_frame = Frame(base, bg='gray')

# Switch to main screen
def show_main_screen():
    welcome_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)

# Welcome screen widgets
Label(welcome_frame, text="Welcome to Encrypt and Decrypt Program", bg='gray', fg='white', font=("Times New Roman", 16, "bold")).pack(pady=50)
Button(welcome_frame, text="Start", bg='lightblue', fg='black', font=("Times New Roman", 14, "bold"), command=show_main_screen).pack(pady=20)
welcome_frame.pack(fill='both', expand=True)

# Main screen widgets
Label(main_frame, text="Enter word text:", bg='gray', fg='white', font=("Times New Roman", 15)).place(x=10, y=45)
entry_word = Entry(main_frame, width=25, bg='gray', fg='white', font=("Times New Roman", 14))
entry_word.place(x=155, y=45)
result_label = Label(main_frame, text="", bg='gray', fg='white', font=("Times New Roman", 15))
result_label.place(x=10, y=75)

# Progress bar (hidden initially)
progress = ttk.Progressbar(main_frame, orient=HORIZONTAL, length=300, mode='determinate')
progress.place(x=75, y=300)
progress.place_forget()

# Simulate progress bar animation
def simulate_progress():
    progress.place(x=75, y=300)
    progress['value'] = 0
    base.update_idletasks()
    for i in range(5):
        progress['value'] += 20
        base.update_idletasks()
        base.after(150)
    progress.place_forget()

# Encrypt text with Caesar cipher
def encryption(text, shift=3):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

# Handle encryption process
def handle_encrypt():
    text = entry_word.get().strip()
    if not text:
        result_label.config(text="Error: Please enter some text!")
    elif len(text) > 25:
        result_label.config(text="Error: Text is too long! (Max: 25 characters)")
    else:
        simulate_progress()
        encrypted_text = encryption(text)
        entry_word.delete(0, END)
        entry_word.insert(0, encrypted_text)
        result_label.config(text="Encrypted word: " + encrypted_text)
        button_save.place(x=300, y=200)
        button_quit.place(x=90, y=200)

# Decrypt text with Caesar cipher
def decryption(text, shift=-3):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

# Handle decryption process
def handle_decrypt():
    text = entry_word.get().strip()
    if not text:
        result_label.config(text="Error: Please enter some text!")
    elif len(text) > 25:
        result_label.config(text="Error: Text is too long! (Max: 25 characters)")
    else:
        simulate_progress()
        decrypted_text = decryption(text)
        entry_word.delete(0, END)
        entry_word.insert(0, decrypted_text)
        result_label.config(text="Decrypted word: " + decrypted_text)
        button_save.place(x=300, y=200)
        button_quit.place(x=90, y=200)

# Save result to file
def save_to_file():
    if not result_label.cget("text"):
        result_label.config(text="Error: No result to save!")
    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(result_label.cget("text"))

# Buttons for saving and quitting (hidden initially)
button_save = Button(main_frame, text="Save as", bg='lightgreen', fg='black', font=("Times New Roman", 12), command=save_to_file)
button_save.place(x=300, y=200)
button_save.place_forget()

button_quit = Button(main_frame, text="Quit", bg='red', fg='white', font=("Times New Roman", 12), command=base.destroy)
button_quit.place(x=90, y=200)
button_quit.place_forget()

# Buttons for encryption and decryption
button_encrypt = Button(main_frame, text="Encrypt", bg='lightblue', fg='black', font=("Times New Roman", 14, "bold"), command=handle_encrypt)
button_encrypt.place(x=90, y=120)

button_decrypt = Button(main_frame, text="Decrypt", bg='lightblue', fg='black', font=("Times New Roman", 14, "bold"), command=handle_decrypt)
button_decrypt.place(x=280, y=120)

# Start the application
base.mainloop()