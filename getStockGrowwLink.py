import json
from nsepython import *
# from nsepython import nse_eq_list

def generate_groww_url(company_name):
    """
    Convert company name to lowercase, hyphenated format for Groww URL
    """
    return "https://groww.in/stocks/" + company_name.strip().lower().replace(" ", "-")

def get_all_stock_data():
    all_data = []
    
    try:
        stock_list = nse_eq_symbols()  # List of stock symbols from NSE
        i=0
        for symbol in stock_list:
            print(i)
            i+=1
            try:
                data = nse_eq(symbol)
                company_name = data['info']['companyName']
                groww_link = generate_groww_url(company_name)
                
                stock_entry = {
                    "symbol": symbol,
                    "company_name": company_name,
                    "groww_url": groww_link
                }
                all_data.append(stock_entry)
            
            except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
    
    except Exception as e:
        print("Error fetching stock list:", e)
    
    return all_data

# Fetch data
stock_data = get_all_stock_data()

# Convert to JSON string (optional)
json_string = json.dumps(stock_data, indent=4)

# Save to file
with open("nse_stocks_with_groww_links.json", "w") as f:
    f.write(json_string)

print("Saved all stock data to 'nse_stocks_with_groww_links.json'")
