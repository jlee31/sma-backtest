import pandas as pd
import matplotlib.pyplot as plt

def calculate_moving_average(data, window=3):
    """
    Calculates the moving average of the given data.
    
    Parameters:
        data (pd.Series): The stock price data.
        window (int): The size of the moving window.
        
    Returns:
        pd.Series: The calculated moving average.
    """
    return data.rolling(window=window).mean()

def plot_data(prices, moving_avg):
    """
    Plots stock prices and their moving average.
    
    Parameters:
        prices (pd.Series): The stock price data.
        moving_avg (pd.Series): The moving average of the stock prices.
    """
    plt.plot(prices, label="Stock Prices")
    plt.plot(moving_avg, label="Moving Average", linestyle='--')
    plt.legend()
    plt.show()

class FinancialAnalysis:
    def __init__(self, data):
        """
        Initializes the financial analysis object.
        
        Parameters:
            data (pd.Series): The stock price data.
        """
        self.data = data

    def moving_average(self, window=3):
        """
        Calculates and returns the moving average.
        
        Parameters:
            window (int): The size of the moving window.
        
        Returns:
            pd.Series: The calculated moving average.
        """
        return calculate_moving_average(self.data, window)

    def plot(self, moving_avg):
        """
        Plots the stock prices and moving average.
        
        Parameters:
            moving_avg (pd.Series): The moving average to plot.
        """
        plot_data(self.data, moving_avg)


# Sample stock data
stock_prices = pd.Series([100, 102, 105, 107, 110, 113, 120])

# Create an instance of the FinancialAnalysis class
analysis = FinancialAnalysis(stock_prices)

# Calculate the moving average with a 3-day window
moving_avg = analysis.moving_average(window=3)

# Plot the stock prices and the moving average
analysis.plot(moving_avg)
