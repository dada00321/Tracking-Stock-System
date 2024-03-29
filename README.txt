﻿1.外部套件安裝
運行本程式需先檢查是否安裝各項套件。
可至以下連結，安裝運行環境相容的各套件「.whl」檔案。
https://www.lfd.uci.edu/~gohlke/pythonlibs/

2. Gmail 存取權限設定
Google基於安全考量,禁止第三方程式存取電子郵件。
因此在本程式「股票通知方式」選單下，選取「(3) 傳送Email」
並按下按鈕後，若無預先設定則會跳出錯誤訊息。

欲更改設定，須至 Google 設定頁面
「低安全性應用程式存取權」
https://myaccount.google.com/lesssecureapps
將 「允許低安全性應用程式」設定為 「已開啟」
方可順利執行。

3.傳送通知按鈕
在IDE運行本程式時，「股票通知方式」選單下之
「傳送股票通知」按鈕，需在第一次按下按鈕時
耐心等待約1秒，第二次按下按鈕後便會陸續判斷
股票資訊、發送通知。

4.股市圖表
在本程式「股市圖表」選單之任一種圖表顯示方式下，
輸入股票代號並按下「確定」鈕後，需關閉視窗，
方可及時在IPython-Console面板顯示股票走勢圖。

5.個人隱私資訊
"Tracking Stock System\modules"
路徑下的:
(1)stock.txt為儲存目標股票代碼、買進賣出價格的文字檔
(2)twilio info.txt為儲存twilio簡訊發送相關個人資訊的文字檔
目的為發送已綁定的個人手機簡訊，即時通知股票訊息；

"Tracking Stock System\modules\res" 路徑下的:
info1.txt, info2.txt, info3.txt
為儲存 Email帳戶資訊的文字檔
目的為發送已綁定的個人Email，即時通知股票訊息。

6.關於第三方API
發送訊息到Line的API為IFTTT公司的套件，可至IFTTT
官方網站做修改:
https://www.ifttt.com

發送訊息到Line的API為Twilio公司的套件，可至Twilio
官方網站做修改:
https://www.twilio.com/
