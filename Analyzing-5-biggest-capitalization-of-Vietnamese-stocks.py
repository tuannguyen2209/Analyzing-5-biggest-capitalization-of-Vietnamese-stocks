import yfinance as yf
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
vn30_stock = ["VCB.VN", "BID.VN", "VHM.VN", "FPT.VN", "HPG.VN"]
stock_data = {}
for stock in vn30_stock:
    print(f"Fetching data for {stock}...")
    data = yf.Ticker(stock)
    stock_data[stock] = data.history(period="3mo", interval="1d")
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 10))
fig.suptitle('VN30 Stock Prices (Last 3 Month)', fontsize=16)
for (stock_symbol, df), ax in zip(stock_data.items(), axes.flat):
    label_name = stock_symbol.replace(".VN", "")
    ax.plot(df.index, df['Close'], label=label_name)
    ax.set_title(label_name)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (VND)")
    ax.grid(color='b', linestyle='-', linewidth=0.1)
    ax.tick_params(axis='x', rotation=30)
for (stock_symbol, df), bx in zip(stock_data.items(), axes.flat):    
    bx.bar(df.index, df['Volume']/1e6, alpha=0.3, color='gray', label='Volume (Million)')
    bx.legend()
axes.flat[-1].axis('off')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()