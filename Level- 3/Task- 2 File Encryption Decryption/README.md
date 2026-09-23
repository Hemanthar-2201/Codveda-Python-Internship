# File Encryption / Decryption Tool

## Description

This project is a command-line Python application that allows users to encrypt and decrypt text files using the Caesar cipher encryption technique.

The application takes a text file from the user, applies a user-defined shift to alphabetic characters, and saves the encrypted content as a new file.

The encrypted file can then be decrypted using the same shift value to recover the original content.

## Features

* Encrypt text files

* Decrypt encrypted text files

* User-defined encryption shift

* Preserve uppercase and lowercase letters

* Preserve spaces, numbers, and special characters

* Save encrypted content as a new file

* Save decrypted content as a new file

* Handle missing files

* Handle permission errors

* Handle invalid shift values

* Provide a simple command-line menu

## Encryption Method

The application uses the **Caesar Cipher**.

In the Caesar cipher, each alphabetic character is shifted by a fixed number of positions in the alphabet.

For example, with a shift of 3:

```
A → D
B → E
C → F
...
X → A
Y → B
Z → C

```

The same process is reversed during decryption.
For example:

```
Original:   HELLO
Shift:      3
Encrypted:  KHOOR

```

Decrypting `KHOOR` with a shift of 3 produces:

```
HELLO

```

## File Handling

The application reads the contents of the input text file and processes the text character by character.
The encrypted or decrypted content is then saved into a new file.

Example:

```
notes.txt
    ↓
Encryption
    ↓
encrypted_notes.txt
    ↓
Decryption
    ↓
decrypted_notes.txt

```

The program uses UTF-8 encoding when reading and writing text files.

## Error Handling

The application handles common errors such as:

* File not found

* Permission denied

* Invalid shift value

* Shift values outside the range 1-25

* Invalid menu choices

* Empty output file name

If the output filename is left empty, the application automatically uses:

`encrypted_file.txt`

for encryption and:

`decrypted_file.txt`

for decryption.

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Create a Text File

Create a text file in the same folder as the Python program.
For example:

`notes.txt`

Add some text to the file.
Example:

```
Hello, this is my private file.
I am learning Python.
This is my encryption task.

```

### 3. Run the Program

Open a terminal in the project folder and run:

```
python "FIle encryption decryption.py"

```

If the filename is changed, use the corresponding filename in the command.

## Example Menu

```

 FILE ENCRYPTION / DECRYPTION TOOL
1. Encrypt a file
2. Decrypt a file
3. Exit
___________________________________
Enter your choice (1-3):

```

## Example Encryption

Select:

`1. Encrypt a file`

Then enter:

```
Enter the file name to encrypt: notes.txt
Enter encryption shift (1-25): 3
Enter the name for the encrypted file: encrypted_notes.txt

```

The program creates:

`encrypted_notes.txt`

containing the encrypted content.

## Example Decryption

Select:

`2. Decrypt a file`

Then enter:

```
Enter the encrypted file name: encrypted_notes.txt
Enter the decryption shift (1-25): 3
Enter the name for the decrypted file: decrypted_notes.txt

```

The program creates:

`decrypted_notes.txt`

with the original text restored.

## Technologies Used

* Python 3

* Caesar Cipher

* File Handling

* String Manipulation

* Command-Line Interface

* Exception Handling

## What I Learned

Through this project, I practiced:

* Creating and using Python functions

* Reading files using Python

* Writing data to files

* Working with text data

* Using character encoding

* Using `ord()` and `chr()` for character conversion

* Applying the Caesar cipher

* Encrypting and decrypting text

* Handling exceptions

* Validating user input

* Building a menu-driven command-line application

## Project Structure

```
Level-3-Task-2/
│
├── FIle encryption decryption.py
├── notes.txt
├── encrypted_notes.txt
├── decrypted_notes.txt
└── README.md

```

Test files such as `notes.txt`, `encrypted_notes.txt`, and `decrypted_notes.txt` are optional. They can be used to demonstrate the encryption and decryption process.

## Limitations

This project is intended as a basic demonstration of file encryption and decryption using the Caesar cipher.
The Caesar cipher is a simple educational encryption technique and should not be used to protect sensitive or confidential information in real-world applications.
The application is designed for text files rather than binary files such as images, videos, or executable files.

## Internship

This project was completed as part of my Python Development Internship at Codveda Technologies.