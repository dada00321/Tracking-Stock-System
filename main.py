from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import re
from Chart import candlestick_chart
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import mpl_finance as mpf
import seaborn as sns
import datetime
import talib
from PIL import Image
###
from matplotlib.backends import tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg

import v1_line as m1
import v2_sms as m2
import v3_email as m3

#######################################
'''Block 1'''
#######################################d

def btn_plot_click():
    hidden_block2()
    candlestick_chart.draw(int(lbl_mode['text']),str(txt_stock.get()))
    
''' Pack and Hidden '''

def pack_block1_v1():
    pack_block1()
    lbl_mode['text'] = '1'
    
def pack_block1_v2():
    pack_block1()
    lbl_mode['text'] = '2'
    
def pack_block1_v3():
    pack_block1()
    lbl_mode['text'] = '3'
    
def pack_block1_v4():
    pack_block1()
    lbl_mode['text'] = '4'
    
def pack_block1():
    hidden_block2()
    lbl_stock.pack()
    txt_stock.pack()
    btn_plot.pack()    
       
def hidden_score_counting_field():
    [widget.pack_forget() for widget in [lbl_stock,txt_stock,btn_plot]]
    
#######################################
'''Block 2'''
#######################################

def pack_block2():
    hidden_score_counting_field()
    btn_send.pack()  
    
def pack_block2_v1():
    pack_block2()
    send_type = 1 # Line
    lbl_send['text'] = 'A'
    
def pack_block2_v2():
    pack_block2()
    send_type = 2 # SMS
    lbl_send['text'] = 'B'
   
def pack_block2_v3():
    pack_block2()
    send_type = 3 # Email
    lbl_send['text'] = 'C'
   
def hidden_block2():
    btn_send.pack_forget()
    
def btn_type():
    if lbl_send['text'] == 'A':
        btn_send['command'] = m1.send_Line
    elif lbl_send['text'] == 'B':
        btn_send['command'] = m2.send_SMS
    elif lbl_send['text'] == 'C':
        btn_send['command'] = m3.send_Email

root = Tk() 
root.geometry("300x100")
root.title("即時股票盯盤細系統")
mainmenu = Menu(root) # mainmenu
root['menu']=mainmenu

###################################################################
plotmenu = Menu(mainmenu) # submenu
mainmenu.add_cascade(label="股市圖表",menu=plotmenu)
mode = IntVar()
plotmenu.add_command(label="(1) 繪製蠟燭",command=pack_block1_v1)
#,command=candlestick_chart.draw(1,'2317')
plotmenu.add_command(label="(2) 加上均線",command=pack_block1_v2)
plotmenu.add_command(label="(3) 加上成交量",command=pack_block1_v3)
plotmenu.add_command(label="(4) 加上KD指標",command=pack_block1_v4)
###########################
stockmenu = Menu(mainmenu) # submenu
mainmenu.add_cascade(label="股票通知方式",menu=stockmenu)
stockmenu.add_command(label="(1) Line通知", command = pack_block2_v1)
stockmenu.add_command(label="(2) 手機簡訊", command = pack_block2_v2)
stockmenu.add_command(label="(3) Email", command = pack_block2_v3)
###########################
exitmenu = Menu(mainmenu) # submenu
mainmenu.add_cascade(label="結束",menu=exitmenu)
exitmenu.add_command(label="離開",command=root.destroy)

###################################################################
###################################################################

lbl_mode  = Label(root, text="")
lbl_stock = Label(root, text="請輸入股票代碼:")
txt_stock = Entry(root, width=10)
btn_plot = Button(root, text="確定", command=btn_plot_click)
canvas = Canvas(root, width=200, height=100)
###########################
global send_type
send_type = IntVar()
btn_send = Button(root, text="傳送即時股票通知", command = btn_type)
lbl_send = Label(root, text="")

root.mainloop()