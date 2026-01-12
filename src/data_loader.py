import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import datetime

# File path: src/data_loader.py

def get_macro_data(start_year=2000):
    """
    Fetches macroeconomic data from FRED and stock market data from Yahoo Finance,
    merges them into a single DataFrame, and performs necessary preprocessing.

    Parameters:
    start_year (int): The starting year for data collection (default: 2000).

    Returns:
    pd.DataFrame: A cleaned DataFrame containing macro indicators and S&P 500 data.
                  Returns None if data collection fails.
    """
    
    # 1. Set Date Range
    start_date = datetime.datetime(start_year, 1, 1)
    end_date = datetime.datetime.now()
    
    print(f"[{datetime.datetime.now().time()}] Starting data collection... (From: {start_year})")

    # 2. Fetch Macro Data from FRED
    # Key: Column name in DataFrame, Value: FRED Series ID
    indicators = {
        'GDP': 'GDP',               # Gross Domestic Product (Quarterly)
        'CPI': 'CPIAUCSL',          # Consumer Price Index for All Urban Consumers (Monthly)
        'Unemployment': 'UNRATE',   # Unemployment Rate (Monthly)
        'Fed_Rate': 'FEDFUNDS',     # Federal Funds Effective Rate (Monthly)
        'US_10Y': 'DGS10',          # 10-Year Treasury Constant Maturity Rate (Daily)
        'US_2Y': 'DGS2',            # 2-Year Treasury Constant Maturity Rate (Daily)
        'M2': 'M2SL'                # M2 Money Stock (Monthly)
    }
    
    try:
        macro_df = web.DataReader(list(indicators.values()), 'fred', start_date, end_date)
        macro_df.columns = list(indicators.keys())
        print(" -> FRED data collection completed.")
    except Exception as e:
        print(f" -> Failed to fetch FRED data: {e}")
        return None

    # 3. Fetch Stock data (NASDAQ & S&P500)
    try:
        tickers = ['^GSPC', '^IXIC']
        stock_raw = yf.download(tickers, start=start_date, end=end_date, progress=False)
        
        if isinstance(stock_raw.columns, pd.MultiIndex):
             # 'Close' 레벨의 데이터만 가져옴
            stock_df = stock_raw['Close']
        else:
            stock_df = stock_raw

        stock_df = stock_df.rename(columns={'^GSPC': 'SP500', '^IXIC': 'Nasdaq'})
        print(" -> Stock market data collection completed.")
    except Exception as e:
        print(f"Failed to fetch stock data: {e}")
        return None

    # 4. Merge and Preprocess
    # Merge on Date index
    df = pd.merge(macro_df, stock_df, left_index=True, right_index=True, how='outer')
    
    # Forward Fill: aligning quarterly/monthly data with daily stock data
    df = df.ffill()
    df = df.dropna()
    
    return df