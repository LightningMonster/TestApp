import pandas as pd
import yfinance as yf
import os

# Load the CSV file
df = pd.read_csv("Collectors/indian_stocks.csv")

# Create a directory to save historical data if it doesn't exist
if not os.path.exists("Collectors/historical_data"):
    os.makedirs("Collectors/historical_data")

# Define the list of periods to fetch data for
periods = ["1d", "5d", "1mo", "6mo", "1y", "5y", "max"]

# Loop through each stock ticker
for index, row in df.iterrows():
    ticker = row["Ticker"]
    print(f"Fetching historical data for {ticker}...")

    try:
        # Loop through each period and overwrite the data if found
        for period in periods:
            print(f"Fetching data for period: {period}")
            
            # Fetch the stock data for the current period
            stock_data = yf.Ticker(ticker)
            historical_data = stock_data.history(period=period, interval="1d")
            
            # If data is found, save it to a CSV and overwrite the file
            if not historical_data.empty:
                historical_data.to_csv(f'test_folder/{ticker}_historical_data.csv')
                print(f"Data for {ticker} (Period: {period}) saved successfully.")
            else:
                print(f"No data available for {ticker} (Period: {period}).")

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")

print("All historical data fetching completed.")
