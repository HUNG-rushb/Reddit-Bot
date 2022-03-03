# !pip install cryptocompare
import cryptocompare
# !pip install datetime
from datetime import date
from datetime import timedelta
import matplotlib.pyplot as plt
import time

today = date.today()

def price_change(crypto_ticker):
  while(1):
    yesterday = today - timedelta(days=1)
    date = yesterday.strftime("%y,%m,%d")
    current_price = cryptocompare.get_price(crypto_ticker)[crypto_ticker]["EUR"]

    yesterday_price = cryptocompare.get_historical_price(crypto_ticker, "EUR", yesterday)[crypto_ticker]["EUR"]

    percent_change = ((current_price - yesterday_price) / yesterday_price) * 100
    change = ""
    if percent_change > 0:
      change = "increase"
    if percent_change < 0:
      change = "decrease"

    print(f"{crypto_ticker} --- {percent_change}% {change} in the last day") 
    print(".")
    time.sleep(3)

# price_change("DOGE")
price_change("BTC")
# price_change("ETH")

