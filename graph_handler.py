import seaborn as sns
import matplotlib.pyplot as plt

def plotter(xdata, ydata):
    sns.scatterplot(x=xdata, y=ydata)
    plt.show()
    return 