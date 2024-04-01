import os
import glob
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import *


def delete_files():
    directory = directory_entry.get()
    file_type = filetype_entry.get()

    files = glob.glob(os.path.join(directory, f'*.{file_type}'))

    for file in files:
        try:
            os.remove(file)
            output_text.insert(tk.END, f'Successfully deleted\n{file}\n')
        except Exception as e:
            output_text.insert(tk.END, f'Error occurred while deleting file {file}. Error message: {e}\n')

    messagebox.showinfo("Info", "Process completed")

def select_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

root = tk.Tk()
root.title("completely delete files in a directory")
root.config(bg="black")

frame1 = tk.Frame(root)
frame1.pack(fill='x')


directory_entry = tk.Entry(frame1)
directory_entry.pack(side='left')
directory_entry.insert(0, 'Enter directory here')

select_directory_button = tk.Button(frame1, text="Select Directory", command=select_directory)
select_directory_button.pack(side='left')

frame2 = tk.Frame(root)
frame2.pack(fill='x')

filetype_entry = tk.Entry(frame2)
filetype_entry.pack(side='left')
filetype_entry.insert(0, 'Enter file type here')

frame3 = tk.Frame(root)
frame3.pack(fill='x')

delete_button = tk.Button(frame3, text="Delete Files", command=delete_files ,bg="red")
delete_button.pack(side='left')

output_text = tk.Text(root)
output_text.pack()

root.mainloop()