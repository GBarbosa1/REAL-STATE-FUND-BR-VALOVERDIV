import yfinance as yf

ifix = yf.Ticker("VALE3.SA")
ifix_hist = vale3.history(start='2022-01-01',end='2023-04-21', interval= '1d')
ifix_hist.reset_index(inplace=True)
