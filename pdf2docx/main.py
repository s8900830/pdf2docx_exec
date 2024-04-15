from pdf2docx import Converter
from tkinter import messagebox
import tkinter as tk
import sys,os

# 轉換本身
def pdf_to_docx(pdf_filepath):
    try:

        # 取得檔名
        docx_filename = os.path.basename(pdf_filepath)
        
        # 製作儲存位置？或是預設同個檔案位置？
        docx_filepath = os.path.abspath(os.getcwd())+f'\\{docx_filename.replace(".pdf","")}.docx'
        
        # 如檔案存在，是否要繼續執行？還是要更改檔名？
        if os.path.exists(docx_filepath):
            print('存在')
            return
        
        # 預備製作輸入密碼的視窗
        cv = Converter(pdf_filepath, password='')

        # 多線程解壓縮，預設 2
        cv.convert(docx_filepath, multi_processing=True, cpu_count=2)

        # 關閉轉換
        cv.close()

        # 轉換完成的訊息視窗
        message(f'轉換完成，路徑為：\n{docx_filepath}','info')

    except Exception as e:
        # 錯誤視窗提醒
        message(e,'error')

def input_secretGUI():
    pass

# 預備資訊欄
def message(msg='',status=''):
    if status =='info':
        messagebox.showinfo('訊息',f'{msg}')
    elif status =='error':
        messagebox.showerror('錯誤',f'{msg}')
    else:
        messagebox.showerror('測試版本','測試版本')
        messagebox.ERROR = 'info'
        pass
    pass

# 要製作LOG嗎？
def log():
    pass

if __name__=='__main__':
    system_argv = sys.argv
    # 重新製作 argv 的內容？

    # 要 API 化嗎？好像可以？

    # 主要執行區段
    if len(system_argv) < 2 :
        print()
    else:
        pdf_to_docx(system_argv[1])
