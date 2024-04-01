import os
import glob
import tkinter as tk
from tkinter import messagebox, filedialog

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

directory_entry = tk.Entry(root)
directory_entry.pack()
directory_entry.insert(0, 'Enter directory here')

select_directory_button = tk.Button(root, text="Select Directory", command=select_directory)
select_directory_button.pack()

filetype_entry = tk.Entry(root)
filetype_entry.pack()
filetype_entry.insert(0, 'Enter file type here')

delete_button = tk.Button(root, text="Delete Files", command=delete_files)
delete_button.pack()

output_text = tk.Text(root)
output_text.pack()

root.mainloop()