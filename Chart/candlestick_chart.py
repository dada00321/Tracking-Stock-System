import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import mpl_finance as mpf
#matplotlib inline
import seaborn as sns
import datetime
import talib
#from PIL import Image


#############################
'''   (5)ALL IN ONE       '''
#############################
def get_figsize(_type):
    _type = int(_type)
    if _type == 1 or _type == 2:
        return (24,8)
    elif _type == 3:
        return (24,15)
    elif _type == 4:
        return (24,20)
    
def draw(candle_type,stock_name):
    
    # (1),(3),(4)會用到
    # 使用pandas_datareader抓取股票
    start = datetime.datetime(2018,4,1)
    df_stock = pdr.DataReader(stock_name+'.TW', 'yahoo', start=start)

    # (1),(4)會用到
    # 使用set_xticklabels來繪製蠟燭
    df_stock.index = df_stock.index.format(formatter=lambda x:x.strftime('%Y-%m-%d'))

    # (1),(2),(3),(4)會用到   
    fig = plt.figure(figsize = get_figsize(candle_type))

    # (2),(3),(4)會用到
    # 簡單移動平均線(SMA)
    sma_10 = talib.SMA(np.array(df_stock['Close']), 10)
    sma_30 = talib.SMA(np.array(df_stock['Close']), 30)

    candle_type = int(candle_type)
    # 畫子圖
    if candle_type == 1 or candle_type == 2:
        ax = fig.add_subplot(1,1,1)
    elif candle_type == 3:
        ax = fig.add_axes([0,0.2,1,0.5])
        ax2 = fig.add_axes([0,0,1,0.2])
    elif candle_type == 4:
        ax = fig.add_axes([0,0.3,1,0.4])
        ax2 = fig.add_axes([0,0.2,1,0.1])
        ax3 = fig.add_axes([0,0,1,0.2])

    # (1),(2),(3),(4)會用到 
    ax.set_xticks(range(0, len(df_stock.index), 10))
    ax.set_xticklabels(df_stock.index[::10])
    mpf.candlestick2_ochl(ax,df_stock['Open'],df_stock['Close'],df_stock['High'],
                  df_stock['Low'],width=0.6,colorup='r',colordown='g',alpha=0.75)

    
    if candle_type in range(2,5):
        # (2),(3),(4) 加上均線
        ax.plot(sma_10, label='MA 10')
        ax.plot(sma_30, label='MA 30')

    if candle_type in range(3,5):
        # (3),(4) 加上成交量
        mpf.volume_overlay(ax2, df_stock['Open'], df_stock['Close'], df_stock['Volume'], colorup='r', colordown='g', width=0.5, alpha=0.8)
        ax2.set_xticks(range(0, len(df_stock.index), 10))
        ax2.set_xticklabels(df_stock.index[::10])

    if candle_type==4:
        # (4)加上KDJ指標
        df_stock['k'], df_stock['d'] = talib.STOCH(df_stock['High'], df_stock['Low'], df_stock['Close'])
        df_stock['k'].fillna(value=0, inplace=True)
        df_stock['d'].fillna(value=0, inplace=True)
        ax3.plot(df_stock['k'], label='K')
        ax3.plot(df_stock['d'], label='D')
        ax3.set_xticks(range(0, len(df_stock.index), 10))
        ax3.set_xticklabels(df_stock.index[::10])
        
    ax.legend()
    fig.savefig('K線圖.png') 
    #im = Image.open('K線圖.png')
    #im.show()

