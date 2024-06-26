import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.io as pio
import os
import matplotlib.dates as mdates
# Ensure the output directory exists
output_dir = os.path.abspath('templates/images')
os.makedirs(output_dir, exist_ok=True)

def perform_eda(df, dataset_name):
    print(f"\n\nPerforming EDA for {dataset_name}")
    
      # 1. Time Series Visualization
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df['Close'], label='Close Price', color='cyan')
    plt.title(f'{dataset_name} - Close Price Over Time', color='white')
    plt.xlabel('Date', color='white')
    plt.ylabel('Price', color='white')
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5, color='grey')
    plt.gca().set_facecolor('black')
    plt.gcf().set_facecolor('black')
    plt.tick_params(colors='white')

    plt.gca().xaxis.set_major_locator(mdates.YearLocator(2))  # Every 2 years
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.xticks(rotation=45) 

    file_path = os.path.join(output_dir, f'{dataset_name}_close_price.png')
    plt.savefig(file_path, facecolor='black')
    plt.close()
    print(f"Saved Close Price plot for {dataset_name} at {file_path}")

    # 3. Pattern Identification: Moving Averages
    
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df['Close'], label='Close Price', color='cyan')
    plt.plot(df.index, df['MA50'], label='50-Day MA', color='orange')
    plt.plot(df.index, df['MA200'], label='200-Day MA', color='red')
    plt.title(f'{dataset_name} - Close Price and Moving Averages', color='white')
    plt.xlabel('Date', color='white')
    plt.ylabel('Price', color='white')
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5, color='grey')
    plt.gca().set_facecolor('black')   # Set the background color of the plot area
    plt.gcf().set_facecolor('black')   # Set the background color of the figure
    plt.tick_params(colors='white')    # Set the tick parameters to be white for visibility

    plt.gca().xaxis.set_major_locator(mdates.YearLocator(2))  # Every 2 years
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.xticks(rotation=45)

    file_path = os.path.join(output_dir, f'{dataset_name}_moving_averages.png')
    plt.savefig(file_path, facecolor='black')
    plt.close()
    print(f"Saved Moving Averages plot for {dataset_name} at {file_path}")

    # 4. Candlestick Chart using Plotly with Dark Background
    file_path = os.path.join(output_dir, f'{dataset_name}_candlestick.html')
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.update_layout(title=f'{dataset_name} - Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      template='plotly_dark',
                      xaxis=dict(tickformat='%Y', tickmode='linear', dtick='M24', tickangle=315))
    pio.write_html(fig, file_path)
    print(f"Saved Candlestick chart for {dataset_name} at {file_path}")

# apple_data = pd.read_csv('datasets/Apple.csv', parse_dates=['Date'])
# def run_eda():
#     perform_eda(apple_data, 'Apple')

def run_eda():
    datasets_path = "datasets/"
    dataset_names = ['Amazon', 'Apple', 'Google', 'Microsoft', 'Netflix']
    datasets_files = ['Amazon.csv', 'Apple.csv', 'Google.csv', 'Microsoft.csv', 'Netflix.csv']

    for dataset_name, dataset_file in zip(dataset_names, datasets_files):
        dataset_path = os.path.join(datasets_path, dataset_file)
        df = pd.read_csv(dataset_path)
        df.set_index('Date')
        perform_eda(df, dataset_name)
