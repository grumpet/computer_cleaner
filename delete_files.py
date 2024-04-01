import os
import glob
import tkinter as tk
from tkinter import messagebox

def delete_files():
    directory = directory_entry.get()
    file_type = filetype_entry.get()

    files = glob.glob(os.path.join(directory, f'*.{file_type}'))

    for file in files:
        try:
            os.remove(file)
            print(f'Successfully deleted {file}')
        except Exception as e:
            print(f'Error occurred while deleting file {file}. Error message: {e}')

    messagebox.showinfo("Info", "Process completed")



root = tk.Tk()

directory_entry = tk.Entry(root)
directory_entry.pack()
directory_entry.insert(0, 'Enter directory here')

filetype_entry = tk.Entry(root)
filetype_entry.pack()
filetype_entry.insert(0, 'Enter file type here')

delete_button = tk.Button(root, text="Delete Files", command=delete_files)
delete_button.pack()

root.mainloop()