import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime
import xlsxwriter

# make software where user can just enter stock name and it will show price


stockCodes = {'Tencent': 'TCEHY', 'Meituan': '3690', 'Alibaba': '9988', 'Wuxi': '2269', 'HKEX': '0388', 'Xiami': '1810'}

stockPrices = {}
cols = ['Stock','Date', 'Open', 'High','Low', 'Close']



headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}



df = pd.DataFrame(columns = cols)


idx = 0
  
  
key = 'Tencent'
value = 'TCEHY'

x = '53'
y = '61'

for i in range(30):
  
            
  url = 'https://finance.yahoo.com/quote/' + f'{stockCodes[key]}' + '/history?p=' + f'{stockCodes[key]}'

  data = requests.get(url, headers=headers, timeout=5)
  soup = BeautifulSoup(data.text, 'html.parser')
  price = soup.find('div', {'class': 'Pb(10px) Ovx(a) W(100%)'})

  

  if (price == None):
     url = 'https://finance.yahoo.com/quote/' + f'{stockCodes[key]}' + '.HK/history?p=' + f'{stockCodes[key]}' + '.HK'

     data = requests.get(url, headers=headers, timeout=5)
     

       
  soup = BeautifulSoup(data.text, 'html.parser')

  price = soup.find('div', {'class': 'Pb(10px) Ovx(a) W(100%)'})
  


  df.loc[idx, 'Stock'] = key 

  if (price == None):
      df.loc[idx, 'Close'] = -1
      df.loc[idx, 'Open'] = -1
      df.loc[idx, 'High'] = -1
      df.loc[idx, 'Low'] = -1
      df.loc[idx, 'Date'] = 'N/A'
    
  else :
    date = price.find('span', {'data-reactid': x})
    Open = price.find('span', {'data-reactid': str(int(y)-6)})
    high = price.find('span', {'data-reactid': str(int(y)-4)})
    low = price.find('span', {'data-reactid': str(int(y)-2)})
    close = price.find('span', {'data-reactid': y})

    if (close == None):
      df.loc[idx, 'Close'] = -1
      
    else:
      close = close.text
      df.loc[idx, 'Close'] = close

    if (Open == None):
      df.loc[idx, 'Open'] = -1
      
    else:
      Open = Open.text
      df.loc[idx, 'Open'] = Open

    if (high == None):
      df.loc[idx, 'High'] = -1
      
    else:
      high = high.text
      df.loc[idx, 'High'] = high

    if (low == None):
      df.loc[idx, 'Low'] = -1
      
    else:
      low = low.text
      df.loc[idx, 'Low'] = low

    if (date == None):
      df.loc[idx, 'Date'] = 'N/A'
      
    else:
      date = date.text
##      print(date[len(date)-2:])
##      print(date[5: 7])
      if (date[0: 3] == 'Sep'):
        df.loc[idx, 'Date'] = '2021-09-' + date[4: 6]
      elif (date[0: 3] == 'Aug'):
        df.loc[idx, 'Date'] = '2021-08-' + date[4: 6]
      else:
        df.loc[idx, 'Date'] = '2021-07-' + date[4: 6]

      

      
      
  idx += 1

 
  x = str(int(x) + 15)
  y = str(int(x) + 8)
   


df.to_csv('StockData.csv', mode = 'a', index = True)



