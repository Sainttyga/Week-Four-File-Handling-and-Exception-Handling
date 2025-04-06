# File Read & Write Program with Error Handling

This Python program demonstrates how to read content from an input file, modify it, and write the modified content to an output file. It also includes error handling for situations where the file may not exist or cannot be accessed.

## Features

- Reads content from an input text file.
- Modifies the content (in this case, converts it to uppercase).
- Writes the modified content to a new output file.
- Includes error handling for missing files, permission issues, and other I/O errors.

## Requirements

- Python 3.x

## Usage

1. Make sure the input file (`input.txt`) is in the same directory as the script, or provide the correct path.
2. Run the script:

   ```bash
   python file_operations.py
3. The script will read the content of input.txt, convert it to uppercase, and write it to output.txt.

Error Handling
FileNotFoundError: If the specified input file is not found.

PermissionError: If the user does not have permission to read or write to the file.

IOError: For any other I/O related errors during file operations.
