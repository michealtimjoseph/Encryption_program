# Encrypt and Decrypt Program

## Overview
The **Encrypt and Decrypt Program** is a simple GUI-based application built using Python's `tkinter` library. It allows users to encrypt and decrypt text using a Caesar cipher. The program also includes features to save the results to a file and provides a progress bar animation for better user experience.

---

## Features
- **Encryption**: Encrypts text using a Caesar cipher with a default shift of 3.
- **Decryption**: Decrypts text using a Caesar cipher with a default shift of -3.
- **Progress Bar**: Displays a progress bar animation during encryption or decryption.
- **Save to File**: Allows users to save the encrypted or decrypted text to a `.txt` file.
- **User-Friendly Interface**: Simple and intuitive GUI for easy interaction.

---

## How to Use
1. **Start the Application**:
   - Run the `encrypt_app.py` file to launch the program.
2. **Enter Text**:
   - On the main screen, enter the text you want to encrypt or decrypt in the input field.
3. **Encrypt or Decrypt**:
   - Click the **Encrypt** button to encrypt the text.
   - Click the **Decrypt** button to decrypt the text.
4. **Save the Result**:
   - After encryption or decryption, click the **Save as** button to save the result to a `.txt` file.
5. **Quit the Application**:
   - Click the **Quit** button to close the program.

---

## Requirements
- Python 3.x
- `tkinter` library (comes pre-installed with Python)
- No additional dependencies are required.
---

## Code Structure
- **Main Window**: Initializes the GUI window and sets up the layout.
- **Welcome Screen**: Displays a welcome message and a "Start" button to proceed to the main screen.
- **Main Screen**:
  - Input field for entering text.
  - Buttons for encryption, decryption, saving results, and quitting.
  - Progress bar for visual feedback during processing.
- **Functions**:
  - `encryption(text, shift)`: Encrypts the input text using a Caesar cipher.
  - `decryption(text, shift)`: Decrypts the input text using a Caesar cipher.
  - `simulate_progress()`: Simulates a progress bar animation.
  - `save_to_file()`: Saves the result to a `.txt` file.

---

## Caesar Cipher Explanation
The Caesar cipher is a substitution cipher that shifts each letter in the plaintext by a fixed number of positions in the alphabet. For example:
- **Encryption**: A shift of 3 turns "A" into "D".
- **Decryption**: A shift of -3 turns "D" back into "A".
---

## Tutorials and Resources
Here are some tutorials and resources to help you understand the concepts used in this program:

- **Python Basics**: [Python Official Documentation](https://docs.python.org/3/tutorial/)
- **Tkinter GUI Programming**: [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- **Caesar Cipher Explanation**: [Caesar Cipher on Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- **File Handling in Python**: [Python File Handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- **Progress Bar in Tkinter**: [Using ttk.Progressbar](https://www.pythontutorial.net/tkinter/tkinter-progressbar/)
- **Creating Buttons and Labels in Tkinter**: [Tkinter Widgets](https://realpython.com/python-gui-tkinter/)

These resources will help you understand the Python and Tkinter concepts used in this program, such as GUI design, event handling, file operations, and encryption techniques.

---

## License
This project is open-source and free to use.

---

## Author
Developed by **Micheal Tim Joseph Enriquez**.  
GitHub Profile: [MichealTimJosephEnriquez](https://github.com/michealtimjoseph)

Instructed by: Mr. Sigred Tong
