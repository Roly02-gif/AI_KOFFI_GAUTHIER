import requests
import pandas as pd
import time

# Timestamps pour les 5 dernieres années
end_time = int(time.time())
start_time = end_time - (5 * 365 * 24 * 60 * 60)  

url = f"https://query1.finance.yahoo.com/v8/finance/chart/BTC-EUR?interval=1d&period1={start_time}&period2={end_time}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    timestamps = data["chart"]["result"][0]["timestamp"]
    open = data["chart"]["result"][0]["indicators"]["quote"][0]["open"]
    high = data["chart"]["result"][0]["indicators"]["quote"][0]["high"]
    low = data["chart"]["result"][0]["indicators"]["quote"][0]["low"]
    close = data["chart"]["result"][0]["indicators"]["quote"][0]["close"]

    df = pd.DataFrame({"date": timestamps, "open": open, "high": high, "low": low, "close": close})
    df["date"] = pd.to_datetime(df["date"], unit="s") 

    df.to_csv("bitcoin_historical_from_2020_to_now.csv", index=False)

    print(df.head())  

else:
    print(f"Erreur {response.status_code}: Impossible de récupérer les données")
    print(response.text)
