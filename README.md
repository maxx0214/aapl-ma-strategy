# AAPL 이동 평균 트레이딩 전략 백테스트

이 프로젝트는 Apple Inc. (`AAPL`) 주식의 데이터를 활용하여, 이동 평균선(MA20, MA60)을 기반으로 한 간단한 매매 전략(골든크로스/데드크로스)을 구현하고, 백테스트를 통해 전략 수익률을 분석하는 프로젝트입니다.

---

## 📊 사용 기술
- Python
- Pandas
- yfinance
- Matplotlib

---

## 📈 전략 개요

- **골든크로스(Golden Cross)**: 단기 이동 평균(MA20)이 장기 이동 평균(MA60)을 상향 돌파할 때 매수
- **데드크로스(Death Cross)**: 단기 이동 평균이 장기 이동 평균을 하향 돌파할 때 매도

---

## 💹 백테스트 결과
![aapl_backtest_plot](https://github.com/user-attachments/assets/abe2331b-38a5-4552-837c-f99592c324e0)
![aapl_strategy_plot](https://github.com/user-attachments/assets/90a6f545-477e-41f5-9924-433a9b7d1217)
![aapl_stock_plot](https://github.com/user-attachments/assets/99e82cc3-36e4-468b-9d31-fcf3feea17ac)


- 누적 수익률 시각화 그래프 포함 (아래 참조)

---

## 📁 파일 설명

| 파일명 | 설명 |
|--------|------|
| `stock_analysis.py` | 데이터 수집 및 시각화 |
| `strategy.py` | 이동 평균 전략 구현 |
| `backtest.py` | 전략 수익률 백테스트 |

---

## 🧠 느낀점

- 단순한 전략이라도 수익률을 시각화해보니 투자 판단에 도움이 됨
- 향후 RSI, MACD 등 다양한 기술 지표도 분석해보고 싶음
