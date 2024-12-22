import yfinance as yf
import json
import datetime

def fetch_stock_data():
    stock_symbols = ["AAPL", "QQQ"]
    results = []
    
    for symbol in stock_symbols:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="6mo")
        
        latest_price = data['Close'][-1]
        latest_volume = data['Volume'][-1]
        dma_50 = data['Close'].rolling(window=50).mean().iloc[-1]
        dma_200 = data['Close'].rolling(window=200).mean().iloc[-1]
        
        results.append({
            "Date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "Stock Symbol": symbol,
            "Latest Price": float(latest_price),
            "Volume": int(latest_volume),
            "50-DMA": float(dma_50),
            "200-DMA": float(dma_200)
        })
    
    # Save as JSON
    with open('stock_data.json', 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    fetch_stock_data()
