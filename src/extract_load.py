import yfinance as yf
import pandas as pd
import dotenv
import os


commodities = ["GC=F","SI=F","CL=F",]

def search_commodity_data(symbol, period="5d", interval="1d"):
    ticker = yf.Ticker('CL=F')
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['Symbol'] = symbol
    return data

def fetch_all_commodities_data(commodities):
    all_data = []
    for symbol in commodities:
        data = search_commodity_data(symbol)
        all_data.append(data)
    return pd.concat(all_data)

if __name__ == "__main__":
    concatenated_data = fetch_all_commodities_data(commodities)
    print(concatenated_data)

