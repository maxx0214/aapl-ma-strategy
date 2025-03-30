import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
data = yf.Ticker("AAPL").history(period="1y")

# 이동 평균
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA60"] = data["Close"].rolling(window=60).mean()

# 매매 시그널 생성
data["Signal"] = 0
data["Signal"][60:] = [
    1 if data["MA20"].iloc[i] > data["MA60"].iloc[i] and data["MA20"].iloc[i-1] <= data["MA60"].iloc[i-1]
    else -1 if data["MA20"].iloc[i] < data["MA60"].iloc[i] and data["MA20"].iloc[i-1] >= data["MA60"].iloc[i-1]
    else 0
    for i in range(60, len(data))
]

# 포지션: 1이면 매수 상태, 0이면 현금 상태
data["Position"] = 0
position = 0
for i in range(len(data)):
    if data["Signal"].iloc[i] == 1:
        position = 1
    elif data["Signal"].iloc[i] == -1:
        position = 0
    data["Position"].iloc[i] = position

# 수익률 계산
data["Daily Return"] = data["Close"].pct_change()
data["Strategy Return"] = data["Daily Return"] * data["Position"]

# 누적 수익률
data["Cumulative Market Return"] = (1 + data["Daily Return"]).cumprod()
data["Cumulative Strategy Return"] = (1 + data["Strategy Return"]).cumprod()

# 그래프로 확인
plt.figure(figsize=(14, 6))
plt.plot(data["Cumulative Market Return"], label="Market Return (Buy & Hold)")
plt.plot(data["Cumulative Strategy Return"], label="Strategy Return (MA Cross)")
plt.title("Backtest: Moving Average Crossover Strategy")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
