from pdf2docx import Converter
from tkinter import messagebox
import os

# 轉換本身


def pdf_to_docx(pdf_filepath):
    try:
        # 製作儲存位置？或是預設同個檔案位置？
        docx_filepath = pdf_filepath.replace(".pdf", ".docx")

        # 如檔案存在，是否要繼續執行？還是要更改檔名？
        if os.path.exists(docx_filepath):
            # print('存在')
            pass

        # 預備製作輸入密碼的視窗
        cv = Converter(pdf_filepath, password='')

        # 發現這邊的多線程有問題，先暫時不使用
        print(cv.convert(docx_filepath, multi_processing=False))

        # 關閉轉換
        cv.close()

        # 回傳路徑
        return docx_filepath

    except Exception as e:
        # 錯誤視窗提醒
        message(e, 'error')


# 提醒視窗
def message(msg='', status=''):
    if status == 'info':
        messagebox.showinfo('訊息', f'{msg}')
    elif status == 'error':
        messagebox.showerror('錯誤', f'{msg}')
    else:
        messagebox.showerror('測試版本', '測試版本')
        messagebox.ERROR = 'info'
        pass


# 要製作LOG嗎？
def log():
    pass


# 測試區段
if __name__ == '__main__':
    # filelist = ['g:\\Python_Training\\github\\pdf2docx_exec\\testfile\\catalog.pdf',
    #             'g:\\Python_Training\\github\\pdf2docx_exec\\testfile\\KSS-Technical_Data-Wirefill_Capacity-TC.pdf']
    
    filelist=["D:\\code\\pdf2docx\\testfile\\進口機車車型耗能證明113年1月核發資料 (1).pdf"]
    # 主要執行區段
    for n in filelist:
        pdf_to_docx(n)
