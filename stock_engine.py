import yfinance as yf
import pandas as pd
import numpy as np

def get_stock_data(symbol):

    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period="1mo", interval="1d")

        if df.empty:
            return None

        df.reset_index(inplace=True)

        # Pandas + NumPy Calculations
        df["Daily_Return"] = df["Close"].pct_change()
        df["Moving_Average"] = df["Close"].rolling(window=5).mean()
        df["Volatility"] = df["Daily_Return"].rolling(window=5).std()

        df.fillna(0, inplace=True)

        latest_price = float(df["Close"].iloc[-1])

        return df.tail(20), latest_price

    except Exception:
        return None