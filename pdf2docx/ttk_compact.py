from tkinter import ttk

class compact:
    def bottom_btn(frame=None,text='',command=None):
        btn=ttk.Button(frame,text=text,command=command,)
        btn.pack(expand=True,side='left')