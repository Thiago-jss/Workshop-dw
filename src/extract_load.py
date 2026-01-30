import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

commodities = ["GC=F","SI=F","CL=F",]



DB_HOST= os.getenv("DB_HOST")
DB_PORT= os.getenv("DB_PORT")
DB_NAME= os.getenv("DB_NAME")
DB_USER= os.getenv("DB_USER")
DB_PASSWORD= os.getenv("DB_PASSWORD")
DB_SCHEMA=os.getenv("DB_SCHEMA")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def search_commodity_data(symbol, period="5d", interval="1d"):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['Symbol'] = symbol
    return data

def fetch_all_commodities_data(commodities):
    all_data = []
    for symbol in commodities:
        data = search_commodity_data(symbol)
        all_data.append(data)
    return pd.concat(all_data)

def save_to_database(df, schema='public' ):
    df.to_sql('commodities', engine,if_exists='replace', index=True, index_label='Date', schema=schema)


if __name__ == "__main__":
    concatenated_data = fetch_all_commodities_data(commodities)
    save_to_database(concatenated_data, schema='public')

