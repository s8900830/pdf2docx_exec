import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttk_compact import compact as ttkc
from tkinter import filedialog as fd
from tkinter import messagebox
import os

class mainprocess:
    def __init__(self):
        self.root =tk.Tk()
        self.root.title('PDF 2 DOCX')
        self.root.iconbitmap=''
        # root.resizable(False, False)
        self.root.geometry('700x500')

        menubar = tk.Menu(self.root)
        menu_file = tk.Menu(menubar,tearoff=False)
        menu_file.add_command(label='Exit',command=self.root.destroy)

        menubar.add_cascade(label='File',menu=menu_file) 
        self.root.config(menu=menubar)

        # 主框架上的表格
        self.main_frame = tk.Frame(border=1,background='#09c')
        self.main_frame.pack(fill="both", expand=1) 

        self.table_scroll_vertical = ttk.Scrollbar(self.main_frame,orient='vertical')
        self.table_scroll_horizontal = ttk.Scrollbar(self.main_frame,orient='horizontal')
        self.table_scroll_vertical.pack(side='right',fill='y')
        self.table_scroll_horizontal.pack(side='bottom',fill='x')

        self.table=ttk.Treeview(self.main_frame,columns=('column1','column2'),show='headings',yscrollcommand=self.table_scroll_vertical.set,xscrollcommand=self.table_scroll_horizontal.set,selectmode='browse')
        # col 的標題
        self.table.heading('column1', text='from')
        self.table.heading('column2', text='to') 
        # 设置表格样式
        self.table.column("column1", width=300,anchor='center')#,stretch=False)
        self.table.column("column2", width=300,anchor='center')#,stretch=False)

        self.table_scroll_vertical.config(command=self.table.yview)
        self.table_scroll_horizontal.config(command=self.table.xview)

        self.table.bind('<Double-Button-1>',function.open_docx_location(self,''))

        self.table.pack(expand=YES, fill=BOTH)


        # 副框架 用來做功能按鈕
        sec_frame = tk.Frame(border=1,background='#09c')
        sec_frame.pack(pady=10) 

        # 把 button 做成另一個 Func，反正都是在底部
        # 這問題我不知道 為什麼要先加入 lambda 函數才不會造成 command 先執行
        # 這邊是有順序的，執行;開啟檔案;離開;更新資料--> 最後這個是為了進度條的功能驗證
        ttkc.bottom_btn(sec_frame,'Execute',lambda:function.input_secretGUI(self))
        ttkc.bottom_btn(sec_frame,'Open File',lambda:function.input_secretGUI(self))
        ttkc.bottom_btn(sec_frame,'Exit',self.root.destroy)
        ttkc.bottom_btn(sec_frame,'update',lambda : function.update(self)) 

        # run the application
        self.root.mainloop()

class function:
    def input_secretGUI(self):
        table=self.table
        filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        
        
        # 放資料
        # table.insert('','end',values=(123,456))
        for n in range(20):
            table.insert('','end',values=(os.path.basename(filename),n))

    def open_docx_location(self,event=None):
        item1 = self.table.focus()
        if item1:
            print (self.table.item(item1))
        pass

    def update(self,id=0,status=''):
        get = self.table.get_children()
        focused = self.table.focus()
        self.table.set(focused,value=('132456','156478'))
        pass

# 是不是要搞個GUI -> 正在做
# 自動排程？

if __name__ == '__main__':
    main = mainprocess()