# File Deletion GUI

This project provides a simple graphical user interface (GUI) for deleting files of a specific type from a specified directory. It's written in Python and uses the `tkinter` module for the GUI.

## Usage

When you run `delete_files.py`, it will display a window with two input fields and a button. 

1. In the first input field, enter the directory from which you want to delete files. The default value is the root of your file system.
2. In the second input field, enter the file type you want to delete (for example, 'pdf' for PDF files).
3. Click the "Delete Files" button to delete all files of the specified type in the specified directory.

The script will display a message box saying "Process completed" when it's done.

## Requirements

This script requires Python 3 and the `tkinter` module, which is included in the standard Python distribution.

## Disclaimer

Please use this script responsibly. It will permanently delete files, so make sure you don't accidentally delete important files. Always double-check the directory and file type before you click the "Delete Files" button.
