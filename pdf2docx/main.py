import sys
import utils
from typing import List


def processing(filelist: List[str]):
    msg = []

    try:
        if len(filelist) == 2:
            msg.append(utils.pdf_to_docx(filelist[1]))
        elif len(filelist) > 2:
            for file in filelist:
                msg.append(utils.pdf_to_docx(file))
        else:
            utils.message(msg='沒有取得任何檔案', status='error')

        # 回傳結果路徑
        utils.message(msg='\n'.join(msg), status='info')

    except Exception as e:

        # 錯誤視窗提醒
        utils.message(msg=e, status='error')


# 主要執行區段
if __name__ == '__main__':
    system_argv = sys.argv
    # 要 API 化嗎？好像可以？

    if len(system_argv) < 2:
        utils.message(msg='沒有取得任何檔案', status='error')
    else:
        # 執行程式
        processing(system_argv)
