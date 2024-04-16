import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import os


def input_secretGUI():

    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    
    
    # 放資料
    # table.insert('','end',values=(123,456))
    for n in range(20):
        table.insert('','end',values=(os.path.basename(filename),n))

    # messagebox.showinfo(
    #     title='Selected File',
    #     message=filename
    # )

def open_docx_location(event):
    item1 = table.focus()
    if item1:
        print (table.item(item1))
    pass


root = tk.Tk()
root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
root.geometry('700x500')

menubar = tk.Menu(root)
menu_1 = tk.Menu(menubar,tearoff=False)
menu_1.add_command(label='Exit',command=root.destroy)

menubar.add_cascade(label='File',menu=menu_1) 

main_frame = tk.Frame(border=1,background='#09c')
main_frame.pack(fill="both", expand=1) 

table_scroll_vertical = ttk.Scrollbar(main_frame,orient='vertical')
table_scroll_horizontal = ttk.Scrollbar(main_frame,orient='horizontal')
table_scroll_vertical.pack(side='right',fill='y')
table_scroll_horizontal.pack(side='bottom',fill='x')

table = ttk.Treeview(main_frame,columns=('column1','column2'),show='headings',yscrollcommand=table_scroll_vertical.set,xscrollcommand=table_scroll_horizontal.set,selectmode='browse')

table.bind('<Double-Button-1>',open_docx_location)

# col 的標題
table.heading('column1', text='from')
table.heading('column2', text='to') 


# 设置表格样式
table.column("column1", width=300,anchor='center')#,stretch=False)
table.column("column2", width=300,anchor='center')#,stretch=False)

table_scroll_vertical.config(command=table.yview)
table_scroll_horizontal.config(command=table.xview)

table.pack(expand=YES, fill=BOTH)

sec_frame = tk.Frame(border=1,background='#09c')
sec_frame.pack(pady=10) 

# exec button
exec_button = ttk.Button(sec_frame,text='Execute',command=input_secretGUI,)
exec_button.pack(expand=True,side='left')

# open button
open_button = ttk.Button(sec_frame,text='Open File',command=input_secretGUI,)
open_button.pack(expand=True,side='left')

# exit button
exit_button = ttk.Button(sec_frame,text='Exit',command=root.destroy,)
exit_button.pack(expand=True,side='left')


root.config(menu=menubar)
# run the application
root.mainloop()

# 是不是要搞個GUI或是自動排程的功能比較好？

if __name__ == '__main__':
    pass
