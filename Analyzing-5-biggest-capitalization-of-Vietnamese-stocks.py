import yfinance as yf
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
vn30_stock = ["VCB.VN", "BID.VN", "VHM.VN", "FPT.VN", "HPG.VN","VIC.VN"]
stock_data = {}
for stock in vn30_stock:
    data = yf.Ticker(stock)
    stock_data[stock] = data.history(period="1y", interval="1d")
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 10), )
fig.suptitle('VN30 Stock Prices (Last 1 Year)', fontsize=16)
for (stock_symbol, df), ax in zip(stock_data.items(), axes.flat):
    delta = df['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    df['MA10'] = df['Close'].rolling(window=10).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    label_name = stock_symbol.replace(".VN", "")
    ax.plot(df.index, df['Close'], label=label_name)
    ax.plot(df.index, df['MA10'], label='MA10', linestyle='--')
    ax.plot(df.index, df['MA50'], label='MA50', linestyle='--')
    ax.set_title(label_name)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (VND)")
    ax.grid(color='b', linestyle='-', linewidth=0.1)
    ax.tick_params(axis='x', rotation=20)
    ax.legend(["Close", "MA10", "MA50"], fontsize=9, loc='upper left')
    ax2 = ax.twinx() # Tạo trục thứ hai dùng chung trục hoành x
    ax2.bar(df.index, df['Volume'], color='gray', alpha=0.6, label='Volume')
    # Cài đặt cho trục thứ hai
    ax2.set_ylabel("Volume", color='gray', fontsize=12)
    # Tắt lưới của trục thứ hai để tránh rối mắt
    ax2.grid(False)
for (stock_symbol, df), ax in zip(stock_data.items(), axes.flat):
    ax3 = ax.twinx() # Tạo trục thứ ba dùng chung trục hoành x
    ax3.spines['right'].set_position(('outward', 60)) # Đưa trục thứ ba ra ngoài
    ax3.plot(df.index, df['RSI'], color='black', label='RSI')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()