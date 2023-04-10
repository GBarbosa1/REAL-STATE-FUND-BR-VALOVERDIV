import seaborn as sns
import matplotlib.pyplot as plt

def plotter(xdata, ydata, title, x_label, y_label, xlim_min, xlim_max, ylim_min, ylim_max, hue):
    fig = plt.figure(figsize=(100,100), dpi = 200)
    sns.set(font_scale = 0.7)
    sns.color_palette("rocket_r", as_cmap=True)
    plot = sns.scatterplot(x=xdata, y=ydata, hue = hue)
    plot.set_title(title, weight = 'bold')
    plot.set_xlabel(x_label, weight = 'bold')
    plot.set_ylabel(y_label, weight = 'bold')
    plot.grid(True)
    plt.show()
    return 
