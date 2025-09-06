import yfinance as yf
import pandas
vn30_stock = ["VCB.VN","BID.VN","VHM.VN","FPT.VN","HPG.VN"]
for stock in vn30_stock:
    data = yf.Ticker(stock)
    df = data.history(period="5y", interval="1d")
    print(f"{stock}:\n{df}\n")
