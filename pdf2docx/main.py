import tkinter as tk
from tkinter import ttk
from time import sleep
from functools import partial
from threading import Thread

running_job = False

def job():
    print("Task started") 
    print("Task completed") 

def experiment():
    while running_job:
        job()
        # I changed it to 1 sec to make it easier to test
        sleep(1)

class GUI:
    def __init__(self,master):
        self.root = master
        self.frame = tk.Frame(self.root)
        self.root.title('PDF 2 DOCX')
        self.root.iconbitmap=''
        self.root.geometry('700x500')

    # Menu 選單
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

        # WTF，還是需要用 lambda 然後要在這邊加入 event 做事件
        self.table.bind('<Double-Button-1>',lambda event: self.open_docx_location(self,event))
        self.table.pack(expand='YES', fill='both')

    # 副框架 用來做功能按鈕
        sec_frame = tk.Frame(border=1,background='#09c')
        sec_frame.pack(pady=10) 

        # 把 button 做成另一個 Func，反正都是在底部
        # 這問題我不知道 為什麼要先加入 lambda 函數才不會造成 command 先執行
        # 這邊是有順序的，執行;開啟檔案;離開;更新資料--> 最後這個是為了進度條的功能驗證
        
        command = partial(run_threaded, experiment)
        exec_button=ttk.Button(sec_frame,text='Execute',command=command)
        exec_button.pack(expand=True,side='left')

        cancel_button=ttk.Button(sec_frame,text='Cancel',command=stop_button)
        cancel_button.pack(expand=True,side='left')

        open_button=ttk.Button(sec_frame,text='Open File',command=lambda:self.input_secretGUI())
        open_button.pack(expand=True,side='left')

        exit_button=ttk.Button(sec_frame,text='Exit',command=self.root.destroy)
        exit_button.pack(expand=True,side='left')


def run_threaded(job_func):
    global running_job
    running_job = True
    job_thread = Thread(target=job_func, daemon=True)
    job_thread.start()

def stop_button():
    global running_job
    running_job = False

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()