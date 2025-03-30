import yfinance as yf
import matplotlib.pyplot as plt

# 애플 데이터 받아오기
apple = yf.Ticker("AAPL")
data = apple.history(period="6mo")  # 최근 6개월

# 이동 평균선 계산 (20일, 60일)
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA60"] = data["Close"].rolling(window=60).mean()

# 그래프 그리기
plt.figure(figsize=(14, 6))
plt.plot(data["Close"], label="Close Price")
plt.plot(data["MA20"], label="MA 20 Days")
plt.plot(data["MA60"], label="MA 60 Days")
plt.title("AAPL Close Price & Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
