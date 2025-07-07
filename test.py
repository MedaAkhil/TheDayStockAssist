
# import requests
# import json
# import time

# def get_nse_stock_data(symbols):
#     base_url = "https://www.nseindia.com/api/quote-equity?symbol=RELIANCE"
#     headers = {
#         "User-Agent": "Mozilla/5.0",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Referer": "https://www.nseindia.com/"
#     }

#     session = requests.Session()
#     session.headers.update(headers)
#     url = base_url.format("RELIANCE")
#     response = session.get(url, timeout=10)
#     print(response)
    # result = []
    # for symbol in symbols:
    #     try:
    #         url = base_url.format(symbol)
    #         response = session.get(url, timeout=10)
    #         if response.status_code != 200:
    #             print(f"Failed to fetch {symbol}: HTTP {response.status_code}")
    #             continue

    #         data = response.json()
    #         current_price = data["priceInfo"].get("lastPrice")
    #         previous_close = data["priceInfo"].get("previousClose")
    #         company_name = data.get("info", {}).get("companyName") or symbol

    #         if current_price and previous_close and previous_close != 0:
    #             growth_rate = ((current_price - previous_close) / previous_close) * 100
    #         else:
    #             growth_rate = None

    #         result.append({
    #             "stock_symbol": symbol,
    #             "stock_name": company_name,
    #             "growth_rate_percent": round(growth_rate, 2) if growth_rate is not None else None
    #         })

    #         time.sleep(0.5)  # Add delay to avoid rate-limit from NSE
    #     except Exception as e:
    #         print(f"Error for {symbol}: {e}")
    #         continue

    # return json.dumps(result, indent=4)
# from nsepython import *

# # Replace with your desired stock symbol
# symbol = "RELIANCE"

# try:
#     stock_data = nse_eq(symbol)
#     print(f"Company Name: {stock_data['info']['companyName']}")
#     print(f"Current Price: {stock_data['priceInfo']['lastPrice']}")
#     print(f"Previous Close: {stock_data['priceInfo']['previousClose']}")
#     print(f"Day High: {stock_data['priceInfo']['intraDayHighLow']['max']}")
#     print(f"Day Low: {stock_data['priceInfo']['intraDayHighLow']['min']}")
# except Exception as e:
#     print(f"Error fetching data: {e}")




from nsepython import *
import json
import time

def get_all_nse_stock_data():
    try:
        # Get all NSE stock symbols
        stock_codes = nse_eq_symbols()
        result = []

        for symbol in stock_codes:
            try:
                stock_data = nse_eq(symbol)

                info = stock_data.get('info', {})
                price_info = stock_data.get('priceInfo', {})

                company_name = info.get('companyName', symbol)
                current_price = price_info.get('lastPrice')
                previous_close = price_info.get('previousClose')

                if current_price is not None and previous_close:
                    growth_rate = ((current_price - previous_close) / previous_close) * 100
                else:
                    growth_rate = None

                result.append({
                    "stock_symbol": symbol,
                    "stock_name": company_name,
                    "current_price": current_price,
                    "previous_close": previous_close,
                    "growth_rate_percent": round(growth_rate, 2) if growth_rate is not None else None
                })

                print(f"✅ Processed: {symbol}")
                time.sleep(0.5)  # avoid hammering the server

            except Exception as e:
                print(f"❌ Error fetching {symbol}: {str(e)}")
                continue

        return result

    except Exception as e:
        print(f"Fatal error: {e}")
        return []

if __name__ == "__main__":
    data = get_all_nse_stock_data()
    with open("nse_stock_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("✅ All stock data saved to nse_stock_data.json")
