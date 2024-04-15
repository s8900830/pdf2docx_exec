import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox


root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def input_secretGUI():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    messagebox.showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=input_secretGUI
)

open_button.pack(expand=True)


# run the application
root.mainloop()

# 是不是要搞個GUI或是自動排程的功能比較好？

if __name__ == '__main__':
    pass
