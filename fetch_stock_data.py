import yfinance as yf
import json
import datetime

def fetch_stock_data():
    stock_symbols = ["AAPL", "QQQ", "SPY", "TSLA", "NVDA"]
    results = []
    
    for index, symbol in enumerate(stock_symbols):
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="6mo")
        
        latest_price = data['Close'][-1]
        latest_volume = data['Volume'][-1]
        avg_volume = data['Volume'].mean()
        dma_50 = data['Close'].rolling(window=50).mean().iloc[-1]
        
        results.append({
            "id": f"{symbol}_{datetime.datetime.now().strftime('%Y%m%d')}",
            "Date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "Stock Symbol": symbol,
            "Latest Price": float(latest_price),
            "Volume": int(latest_volume),
            "Average Volume": int(avg_volume),
            "50-DMA": float(dma_50)
        })
    
    # Save as JSON
    with open('stock_data.json', 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    fetch_stock_data()
