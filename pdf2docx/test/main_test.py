import tkinter as tk
from time import sleep
from functools import partial
from threading import Thread
from .. import utils

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
        self.master = master
        self.frame = tk.Frame(self.master)

        command = partial(run_threaded, experiment)
        self.button1 = tk.Button(text="Start", command=command)
        self.button1.pack()
        self.button2 = tk.Button(text="Stop", command=stop_button)
        self.button2.pack()


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