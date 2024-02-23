import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def plot_stock_chart(stock_data):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plotting candlestick chart
    ax.plot(stock_data.index, stock_data['Close'], label='Closing Price', color='black', alpha=0.5)

    # Plotting 50-day and 200-day moving averages
    stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()
    ax.plot(stock_data.index, stock_data['MA50'], label='50-day MA', color='blue')
    ax.plot(stock_data.index, stock_data['MA200'], label='200-day MA', color='red')

    # Plotting up and down days as candles
    for i in range(1, len(stock_data)):
        if stock_data['Close'][i] > stock_data['Close'][i-1]:
            color = 'g'  # Green candle for up day
        else:
            color = 'r'  # Red candle for down day

        ax.plot([stock_data.index[i], stock_data.index[i]],
                [stock_data['Low'][i], stock_data['High'][i]],
                color=color)

    # Marking the crosses of 50-day and 200-day moving averages
    crosses = stock_data[stock_data['MA50'] > stock_data['MA200']].index
    ax.plot(crosses, stock_data.loc[crosses, 'MA50'], '^', markersize=10, color='g', label='50-day cross above 200-day')
    
    crosses = stock_data[stock_data['MA50'] < stock_data['MA200']].index
    ax.plot(crosses, stock_data.loc[crosses, 'MA50'], 'v', markersize=10, color='r', label='50-day cross below 200-day')

    # Adding labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')
    ax.set_title('Microsoft Stock Analysis')

    # Adding legend
    ax.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    ticker = 'MSFT'
    start_date = '2014-02-23'  # Change this to the desired start date
    end_date = '2024-02-23'    # Change this to the desired end date

    stock_data = fetch_stock_data(ticker, start_date, end_date)
    plot_stock_chart(stock_data)
