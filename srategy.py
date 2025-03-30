import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 불러오기
apple = yf.Ticker("AAPL")
data = apple.history(period="6mo")

# 이동 평균선
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA60"] = data["Close"].rolling(window=60).mean()

# 매매 신호 컬럼
data["Signal"] = 0
data["Signal"][20:] = \
    [1 if data["MA20"].iloc[i] > data["MA60"].iloc[i] and data["MA20"].iloc[i-1] <= data["MA60"].iloc[i-1]
     else -1 if data["MA20"].iloc[i] < data["MA60"].iloc[i] and data["MA20"].iloc[i-1] >= data["MA60"].iloc[i-1]
     else 0
     for i in range(20, len(data))]

# 매수/매도 위치 저장
buy_signals = data[data["Signal"] == 1]
sell_signals = data[data["Signal"] == -1]

# 그래프 그리기
plt.figure(figsize=(14, 6))
plt.plot(data["Close"], label="Close Price", alpha=0.5)
plt.plot(data["MA20"], label="MA 20 Days", linewidth=1.5)
plt.plot(data["MA60"], label="MA 60 Days", linewidth=1.5)

# 매수/매도 표시
plt.scatter(buy_signals.index, buy_signals["Close"], marker="^", color="green", label="Buy Signal", s=100)
plt.scatter(sell_signals.index, sell_signals["Close"], marker="v", color="red", label="Sell Signal", s=100)

plt.title("AAPL Moving Average Strategy")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
