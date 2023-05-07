import yfinance as yf

def yfinance (tick_name, init_date, end_date,interval):
    ticker = yf.Ticker(tick_name)
    ticker_hist = ticker.history(start=init_date,end=end_date, interval=interval)
    ticker_hist.reset_index(inplace=True)
    return ticker_hist

df = yfinance('VALE3.SA', '2023-01-01', '2023-05-01', '1d')
df.to_csv('test.csv')
