import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_file(filename: str) -> str:
    """Read the content of a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"The file '{filename}' was not found.")
        return ""
    except PermissionError:
        logging.error(f"You do not have permission to read the file '{filename}'.")
        return ""
    except IOError as e:
        logging.error(f"An error occurred while reading the file: {e}")
        return ""

def write_file(filename: str, content: str) -> None:
    """Write content to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        logging.info(f"Content successfully written to {filename}")
    except IOError as e:
        logging.error(f"An error occurred while writing to the file: {e}")

def read_and_write_file(input_filename: str, output_filename: str) -> None:
    """Read from one file, modify the content, and write to another file."""
    content = read_file(input_filename)
    if content:
        modified_content = content.upper()
        write_file(output_filename, modified_content)

def ask_for_filename() -> None:
    """Prompt the user for a filename and display its content."""
    while True:
        filename = input("Please enter the filename to read: ")
        content = read_file(filename)
        if content:
            print(f"File content:\n{content}")
            break

if __name__ == "__main__":
    # Example usage
    read_and_write_file('input.txt', 'output.txt')
    ask_for_filename()text