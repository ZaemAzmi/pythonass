import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.io as pio
import os

# Ensure the directory exists
output_dir = os.path.abspath('templates/images')
os.makedirs(output_dir, exist_ok=True)

def perform_eda(df, dataset_name):
    print(f"\n\nPerforming EDA for {dataset_name}")

    # Create a figure with subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'{dataset_name} - Stock Analysis')

    # Time Series Visualization
    axs[0, 0].plot(df.index, df['Close'], label='Close Price')
    axs[0, 0].set_title('Close Price Over Time')
    axs[0, 0].set_xlabel('Date')
    axs[0, 0].set_ylabel('Price')
    axs[0, 0].legend()

    # Correlation Analysis
    corr_matrix = df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=axs[0, 1])
    axs[0, 1].set_title('Correlation Matrix')

    # Pattern Identification
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()
    axs[1, 0].plot(df.index, df['Close'], label='Close Price')
    axs[1, 0].plot(df.index, df['MA50'], label='50-Day MA', color='orange')
    axs[1, 0].plot(df.index, df['MA200'], label='200-Day MA', color='red')
    axs[1, 0].set_title('Stock Close Price and Moving Averages')
    axs[1, 0].set_xlabel('Date')
    axs[1, 0].set_ylabel('Price')
    axs[1, 0].legend()

    # Save the figure
    file_path = os.path.join(output_dir, f'{dataset_name}_summary.png')
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(file_path)
    plt.close()
    print(f"Saved summary plot for {dataset_name} at {file_path}")

    # Advanced Visualization: Candlestick Chart
    file_path = os.path.join(output_dir, f'{dataset_name}_candlestick.html')
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.update_layout(title=f'{dataset_name} - Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price')
    pio.write_html(fig, file_path)
    print(f"Saved Candlestick chart for {dataset_name} at {file_path}")

def run_eda():
    datasets_path = "pythonass/datasets/"
    dataset_names = ['Amazon', 'Apple', 'Google', 'Microsoft', 'Netflix']
    datasets_files = ['Amazon.csv', 'Apple.csv', 'Google.csv', 'Microsoft.csv', 'Netflix.csv']

    for dataset_name, dataset_file in zip(dataset_names, datasets_files):
        dataset_path = os.path.join(datasets_path, dataset_file)
        df = pd.read_csv(dataset_path)
        perform_eda(df, dataset_name)
