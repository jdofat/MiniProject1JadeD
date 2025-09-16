# INF601 - Advanced Programming in Python

# Jade Dofat

# Mini Project 1


"""
Video:
https://www.youtube.com/watch?v=-LZS9UcGKjw&list=PLE5nOs3YmC2TeLcNOxFXKCzVfGb6MJri4&index=2

✅(5/5 points) Proper import of packages used.
"""
import yfinance as yf
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import pprint
import copy
import os

os.makedirs("charts", exist_ok=True)

tickers = ["KO", "PEP", "MCD", "SBUX", "MDLZ"]
tickersdata = {}

for stock in tickers:
    data = yf.Ticker(stock)
    last10 = data.history(period="11d")
    last10 = last10.iloc[:-1]

    tickersdata[stock] = []
    for price in last10["Close"]:
        tickersdata[stock].append(price)
    print(last10["Close"])
    mystock = np.array(tickersdata[stock])

    highlow = copy.copy(tickersdata[stock])
    highlow.sort()

    plt.figure()
    plt.title(f"{stock} Closing Prices Last 10 Days")
    plt.plot(mystock)

    plt.xticks(ticks=range(10), labels=range(1, 11))
    plt.axis((0, 9, highlow[0]-3, highlow[-1]+3))
    plt.xlabel("X Days Ago")
    plt.ylabel("Closing Price")

    plt.savefig(f"charts/{stock}_closing_prices.png")
    plt.close()


"""
✅(20/20 points)
Using an API of your choice (yfinance works)
-collect the closing price of 5 of your favorite stock tickers
for the last 10 trading days:
-Coca Cola, Pepsi, McDonalda, Starbucks, and Mondelez Int.

✅(10/10 points)
Store this information in a list that you will convert to an array in NumPy.


✅(10/10 points)
Plot these 5 graphs:
-Feel free to add information.
-At minimum it just needs to show 10 data points.

(10/10 points)
Save these graphs in a folder called charts as PNG files
-Do not upload these to your project folder
-the project should save these when it executes
-You may want to add this folder to your .gitignore file.

(10/10 points) In the main branch of your project:
-Please be sure to include a requirements.txt file which contains all the packages that need installed
-You can create this file with the output of pip freeze at the terminal prompt.

(20/20 points) There should be a README.md file in your project that explains:
-what your project is
-how to install the pip requirements
-how to execute the program
-Please use the GitHub flavor of Markdown.

"""