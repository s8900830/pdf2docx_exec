import tkinter as tk
from tkinter import *
from tkinter import ttk
from pdf2docx.gui.ttk_compact import compact as ttkc
from tkinter import filedialog as fd
from tkinter import messagebox
from threading import Thread
import os,utils,time

class MainProcess:
    def input_secretGUI(self):
        table=self.table
        filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)

        self.pdffilelist.append(filename)
        self.docxfilelist.append(filename.replace(".pdf", ".docx"))

        # 放資料
        # for n in range(20):
        #     table.insert('','end',values=(os.path.basename(filename),f'Not Start'))

        table.insert('','end',values=(os.path.basename(filename),f'Not Start'))

    def open_docx_location(self,event=None):
        # 看要怎麼取轉換後的路徑，我已經先存在 docxlist 內？
        item1 = self.table.focus()
        if item1:
            print (self.table.item(item1))
            # print (self.table.item(item1))
        pass
    
    def schedule_check(self,t):
        """
        Schedule the execution of the `check_if_done()` function after
        one second.
        """
        self.root.after(1000, self.check_if_done, t)

    def check_if_done(self,t):
        if not t.is_alive():
            pass
        else:
            self.schedule_check(self,t)

    def start_task(self):
        t = Thread(target=self.run_pdf2docx())
        t.start()
        self.schedule_check(t=t)

    def run_pdf2docx(self):
        utils.pdf_to_docx()

        
    def stop_task(self):
        t = False

    # def update(self,id='',status=''):
    #     get = self.table.get_children()
    #     for n in get:
    #         selected_item = self.table.item(n)
    #         # exec pdf2docx
    #         self.table.item(n,values=('','25'))
    #     # self.table.set(focused,colume='I001',value='112233')
    #     pass

# 是不是要搞個GUI -> 正在做
# 自動排程？

if __name__ == '__main__':
    main = MainProcess()