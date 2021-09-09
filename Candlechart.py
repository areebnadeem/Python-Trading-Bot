import pandas as pd
import mplfinance as mpf

df = pd.read_csv('StockData.csv', index_col = 1)

##df = df[:8]

####
##df = pd.DataFrame([
##    ['2021-02-01', 595.00,612.00,587.00,611.00],
##    ['2021-02-02',629.00,638.00,622.00,632.00],
##    ['2021-02-03',638.00,642.00,630.00,630.00],
##    ['2021-02-04',626.00,632.00,620.00,627.00],
##    ['2021-02-05',638.00,641.00,631.00,632.00],
##
##], columns=['Date','Open', 'High', 'Low', 'Close'])
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
df.set_index('Date', inplace=True)


mpf.plot(df, type='candle', title='Tencent')

