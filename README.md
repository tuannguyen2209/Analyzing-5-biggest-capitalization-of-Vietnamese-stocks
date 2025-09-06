# An Analysis of Vietnam's Top 6 Largest Stocks by Market Capitalization

**Author:** Nguyen Anh Tuan  
**Date:** September 6, 2025  
**GitHub Repository:** https://github.com/tuannguyen2209

---

## 1. Project Overview

### 1.1. Introduction
This project presents a quantitative analysis of the top six largest publicly traded companies in Vietnam by market capitalization. The study examines key financial metrics, including historical price movements, trading volumes, and standard technical indicators. The primary objective is to derive actionable insights into the behavior and trends of these market-leading equities. This project serves as a practical application of data analysis techniques using Python and foundational libraries within its ecosystem.

### 1.2. Scope of Analysis
* **Equities Analyzed:** VCB, BID, VHM, FPT, HPG, ACV
* **Time Period:** 1 Year (From September 6, 2024, to September 6, 2025)
* **Data Granularity:** Daily (1d)

---

## 2. Methodology & Technical Stack

### 2.1. Technical Stack
The analysis was conducted using the following technologies:
* **Programming Language:** Python (v3.9)
* **Core Libraries:**
    * `pandas` for data manipulation and analysis.
    * `numpy` for numerical operations.
    * `yfinance` for financial data acquisition.
    * `matplotlib` for data visualization.
* **Development Environment:** Jupyter Notebook, VS Code

### 2.2. Data Analysis Workflow

#### 2.2.1. Data Acquisition
Historical stock data for the selected tickers was programmatically acquired from Yahoo Finance via the `yfinance` API. For each of the six equities, a time-series dataset was collected, containing daily Open, High, Low, Close (OHLC) prices and trading Volume. Each resulting DataFrame consists of approximately 250 records, corresponding to the number of trading days in the specified one-year period.

#### 2.2.2. Data Preprocessing & Feature Engineering
The raw data obtained from `yfinance` is well-structured and required minimal cleaning. The primary focus of this stage was feature engineering—calculating standard technical indicators to support the analysis.

**a) Simple Moving Averages (SMA)**

Two Simple Moving Averages were computed for the daily closing price (`Close`):
* **MA10:** A 10-day SMA, calculated using the `rolling(window=10).mean()` method in pandas to determine the short-term trend.
* **MA50:** A 50-day SMA, calculated using `rolling(window=50).mean()` to identify the medium-term trend.

**b) Relative Strength Index (RSI)**

The 14-day RSI, a momentum oscillator, was calculated through the following sequence of operations:
1.  **Price Change (`delta`):** The daily price change was computed using the `diff(1)` method.
2.  **Gains & Losses:** Positive price changes (`gain`) and the absolute value of negative price changes (`loss`) were isolated using the `where()` method.
3.  **Average Gain/Loss:** A 14-day rolling average was applied to both the `gain` and `loss` series to smooth the data.
4.  **Relative Strength (RS):** The ratio of the average gain to the average loss was calculated.
5.  **RSI Calculation:** The final RSI value was normalized to an oscillator scale of 0 to 100 using the standard formula: `100 - (100 / (1 + RS))`.

---

## 3. Installation and Replication

Instructions to replicate this analysis locally.

### Prerequisites
* Python 3.9+
* Git

### Installation Steps

```bash
# 1. Clone the repository
git clone [https://github.com/tuannguyen2209/Analyzing-6-biggest-capitalization-of-Vietnamese-stocks.git](https://github.com/tuannguyen2209/Analyzing-6-biggest-capitalization-of-Vietnamese-stocks.git)

# 2. Navigate to the project directory
cd Analyzing-6-biggest-capitalization-of-Vietnamese-stocks

# 3. Install the required dependencies
pip install -r requirements.txt
### Installation Steps
