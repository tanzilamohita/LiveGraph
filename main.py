import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
from matplotlib import style
from pandas.plotting import register_matplotlib_converters

style.use('fivethirtyeight')

fig = plt.figure(figsize=(10, 6))
#ax1 = fig.add_subplot(1, 1, 1)
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.05, 0.65, 0.5, 0.3])


def animate(i):
    stock_data = pd.read_csv('datasets/stocks.csv')
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    fig.suptitle('AAPL vs IBM')

    xs_ax1 = stock_data['Date']
    ys_ax1 = stock_data['AAPL']

    xs_ax2 = stock_data['Date']
    ys_ax2 = stock_data['IBM']

    ax1.clear()
    ax1.plot(xs_ax1, ys_ax1, color='green')
    ax1.plot()
    ax2.clear()
    ax2.plot(xs_ax2, ys_ax2, color='blue')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

