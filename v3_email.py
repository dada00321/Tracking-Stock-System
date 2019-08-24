import time
from modules import *
import modules.stock_module as m

def send_Email():
    slist = m.get_setting()
    count = len(slist) #計算有幾支股票

    log1=[] #紀錄傳送過的股價高於or低於期望價的訊息,避免重複傳送
    log2=[] #紀錄傳送過的符合4大買賣點的訊息,避免重複傳送
    for i in range(count):
        log1.append('')
        log2.append('')
    check_times = 20 #指定檢查幾次(20*3mins=60mins)
    while True:
        for i in range(count):
            stock_id, low, high = slist[i] #讀取股票代號、期望買進價、期望賣出價        
            name, price = m.get_price(stock_id) #讀取股票名稱、即時股價
            act = ""; status = "" ; base_point = 0
            print('檢查:',name,'股價:',price,'區間',low,'~',high)
            if price<=low: #買進時機
                if log1[i] != '買進':
                    ''' m.send_ifttt(name,price,'買進(股價低於%s)'%str(low))'''
                    act = "買進"; status = "低"
                    log1[i] = '買進'   #記錄下來,避免重複
                    base_point = low
                    
            elif price>=high: #賣出時機
                if log1[i] != '賣出':
                    ''' m.send_ifttt(name,price,'賣出(股價高於%s)'%str(high))'''
                    act = "賣出"; status = "高"
                    log1[i] = '賣出'   #記錄下來,避免重複
                    base_point = high
                    
            contents = (name+"股價:"+str(price)+
                        "\n建議操作:"+act+"(股價"+status+"於"+str(base_point))
            m.send_email(contents) ###
            
            ''' '''
            act, reason = m.get_best(stock_id) #檢查四大買賣點
            if reason: #若符合四大買賣點
                if log2[i] != reason:
                    ''' m.send_ifttt(name,price,act+'('+reason+')')'''
                    contents = (name+"股價:"+str(price)+ 
                                "\n建議操作:"+act+'('+reason+')')
                    m.send_email(contents) ###
                    
                    log2[i] = reason   #記錄下來,避免重複
        print("============================")
        check_times-=1 #檢查用計數器-1
        if check_times==0: break
        time.sleep(180) #每180sec(3mins)檢查一遍(查看最新股票資訊)