import json
from nsetools import Nse
import yfinance as yf


def getListOfNseCompanies():
    nse = Nse()
    stock_list = nse.get_stock_codes()
   # stock_list = stock_list[0:10]
    if not isinstance(stock_list, list):
        raise TypeError("Expected list from nse.get_stock_codes(), got something else.")

    result = []

    for symbol in stock_list:
        try:
            ticker = yf.Ticker(f"{symbol}.NS")
            info = ticker.info

            current_price = info.get("currentPrice")
            previous_close = info.get("previousClose")

            if current_price and previous_close and previous_close != 0:
                growth_rate = ((current_price - previous_close) / previous_close) * 100
                # if(not(growth_rate < 1)): break
            else:
                growth_rate = None
            company_name = info.get("longName") or info.get("shortName") or symbol

            result.append({
                "stock_symbol": symbol,
                "stock_name": company_name,
                "growth_rate_percent": round(growth_rate, 2) if growth_rate is not None else None
            })
    
        except Exception:
            continue  # Skip if error in fetching stock data
    print(result )
    return json.dumps(result, indent=4)

# Example usage
if __name__ == "__main__":
    print(getListOfNseCompanies(limit=10))
