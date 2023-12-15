import pyperclip
import os
import sys

# Get the selected text from the clipboard
selected_text = pyperclip.paste()

# Determine the path to the folder where the script or executable is located
if getattr(sys, 'frozen', False):
    # The script is frozen (compiled with PyInstaller)
    folder_path = os.path.dirname(sys.executable)
else:
    # The script is not frozen
    folder_path = os.path.dirname(os.path.abspath(__file__))

# Set the file name
file_name = 'links.txt'

# Construct the full path to the file
file_path = os.path.join(folder_path, file_name)

# Read the existing content of the file
try:
    with open(file_path, 'r') as file:
        existing_text = file.read()
except FileNotFoundError:
    existing_text = ''

# Append the selected text after the existing content
with open(file_path, 'a') as file:
    if existing_text:
        # If the file already has text, add a newline before appending
        file.write('\n')
    file.write(selected_text)
