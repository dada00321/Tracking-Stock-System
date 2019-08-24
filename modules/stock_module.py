import twstock
import requests
from twilio.rest import Client                  #簡訊
import smtplib                                  #email
from email.mime.multipart import MIMEMultipart  #email
from email.mime.text import MIMEText            #email
from modules.res import read_info

def get_setting(): #剖析txt檔,回傳股票代號、期望買進價、期望賣出價
    res=[]
    try:
        with open('modules\\stock.txt') as f:
            slist = f.readlines()
            print("讀入:",slist)
            for lst in slist:
                s=lst.split(',')
                res.append([s[0].strip(),float(s[1]),float(s[2])])
    except:
        print("讀取錯誤")

    return res

def send_ifttt(v1,v2,v3): #向IFTTT發送http request的函式
    #參數:name,price,suggestion
    url=("https://maker.ifttt.com/trigger/toLine/with/"+
    "key/cI7cOoeaBwfkOMXAmmm86-z6t_tpIpKZQnI6bbKlTci"+
    "?value1="+ str(v1) +
    "&value2="+ str(v2) +
    "&value3="+ str(v3))

    r = requests.get(url)
    '''回應文字以Congr開頭則代表成功。
    因先前在IFTTT設定if傳送http請求then發訊息到line
    用r來接requests的傳回值,若成功應為"Congratulations! ..."
    '''
    if r.text[:5]=="Congr": 
        print("已傳送(%s,%s,%s)到Line!"%(str(v1),str(v2),str(v3)))
    return r.text

def send_sms(contents):
    with open('modules\\twilio info.txt','r') as fp:
        data = fp.readlines()
        mySid = data[0]
        myToken = data[1]

        client = Client(mySid,myToken)
        msg = client.messages.create(
                from_ = data[2],
                to = data[3],
                body = contents)
def send_email(contents):
    # Gamil信箱資訊
    account,password = read_info.read()
    host = "smtp.gmail.com" #mail server的網址
    from_email = account
    to_list = [account] #傳給自己測試

    mySmtp = smtplib.SMTP(host,587)
    mySmtp.starttls()
    print(mySmtp.login(account,password)) #登入

    # Create message container - the correct MIME type is multipart/alternative.
    the_msg = MIMEMultipart("alternative")
 
    # 開始郵件內容
    the_msg["Subject"] = "【股票通知】"
    the_msg["From"] = from_email
    the_msg["To"] = to_list[0]

    plain_txt = contents
    mainText = MIMEText(plain_txt, 'plain', 'utf-8')
    the_msg.attach(mainText)
    
    print(the_msg.as_string()) # 檢查信件內容
    mySmtp.sendmail(from_email, to_list, the_msg.as_string()) # 發送信件
    mySmtp.quit()

def get_price(stock_id): #參數:股票代碼 回傳:股票名稱、即時股價
    rt = twstock.realtime.get(stock_id) #以股票代碼建立讀取資訊物件rt
    if rt['success']:
        return (rt['info']['name'],
                float(rt['realtime']['latest_trade_price']))
    else:
        return (False,False)
    
def get_best(stock_id): #參數:股票代碼 回傳:建議(買/賣)、建議資訊
    stock = twstock.Stock(stock_id) #以股票代碼建立Stock物件
    bp = twstock.BestFourPoint(stock).best_four_point()
    '''回傳檢測四大買賣點資訊給bp
    bp為tuple型態,若適合買進bp[0]為True,否則為False
    bp[1]則是建議買/賣的原因(字串)'''
    
    if (bp):
        return ('買進' if bp[0] else '賣出',bp[1])
    else:
        return (False,False)