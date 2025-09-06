# Analyzing-5-biggest-capitalization-of-Vietnamese-stocks
#### Author: Nguyen Anh Tuan
#### Completion Date: September 06, 2025
#### GitHub Repository: https://github.com/tuannguyen2209
----- 
# 1) Project Description
This is my first project in my path of being a data sciencetist. This project will analyze top 5 largest Vietnamese stocks thought Volume, Price capitaliztion by real-time update data for 1 year from 01-01-2025 to 06-09-2025. Beside that, this project will give you some interesting insight about Vietnamese stocks. After this project will have been done, I will gain more experience in how to use pandas,yfinance, matplotlib, more and more.
## Top 5 largest Vietnamese stocks by market capitalization:
1) VCB (Ngân hàng TMCP Ngoại thương Việt Nam - Vietcombank)
2) BID (Ngân hàng TMCP Đầu tư và Phát triển Việt Nam - BIDV)
3) VHM (Công ty Cổ phần Vinhomes)
4) FPT (Công ty Cổ phần FPT)
5) HPG (Tập đoàn Hòa Phát)
----- 
# 2) Tech Stack
List the main tools, languages, and libraries used in this project.
- Language: Python (v3.9)
- Libraries: Pandas, NumPy, Matplotlib
- Environment: Jupyter Notebook, VS Code
-----
# 3) Installation & Usage
Instructions on how others can set up and run your project locally.
### Prerequisites
* Python 3.9+
* Git
-----
# 4) Data Analysis Workflow
## 4.1) Data Collection & Exploratory Data Analysis (EDA)
- I have 5 different stocks so I will use yfinance library to collect data which include Date, Open, High, Low, Close, Volume into 5 different dataframes.
- each dataframe has 250 rows and 7 collums.
- The key variables are SMA,RSI and Volume. They will present the trend of 5 stocks. 
### Installation Steps
```bash
# 1. Clone a copy of the repository
git clone [[https://github.com/your-username/your-project.git](https://github.com/your-username/your-project.git)](https://github.com/tuannguyen2209/Analyzing-5-biggest-capitalization-of-Vietnamese-stocks.git)
# 2. Navigate to the project directory
cd your-project
# 3. Install the required dependencies
pip install -r requirements.txt
