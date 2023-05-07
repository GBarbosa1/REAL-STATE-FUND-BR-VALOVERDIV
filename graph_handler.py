import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plotter_with_hoover(xdata, ydata, value, asset_name, title, xlabel, ylabel):
    colors = np.random.randint(1, 5, size=len(xdata))
    norm = plt.Normalize(1, 4)
    cmap = plt.cm.PiYG
    fig, ax = plt.subplots()
    plt.subplot(121)
    scatter = plt.scatter(
        x=xdata,
        s = value,
        y=ydata)
    annotation = ax.annotate(
    text='',
    xy=(0, 0),
    xytext=(15, 15),
    textcoords='offset points',
    bbox={'boxstyle': 'round', 'fc': 'w'},
    arrowprops={'arrowstyle': '->'}
    )
    annotation.set_visible(False)
    def motion_hover(event):
        annotation_visbility = annotation.get_visible()
        if event.inaxes == ax:
            is_contained, annotation_index = scatter.contains(event)
            if is_contained:
                data_point_location = scatter.get_offsets()[annotation_index['ind'][0]]
                annotation.xy = data_point_location
                text_label = (asset_name.iloc[annotation_index['ind'][0]])
                annotation.set_text(text_label)
                annotation.get_bbox_patch().set_facecolor(cmap(norm(colors[annotation_index['ind'][0]])))
                annotation.set_alpha(0.4)
                annotation.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if annotation_visbility:
                    annotation.set_visible(False)
                    fig.canvas.draw_idle()
    fig.canvas.mpl_connect('motion_notify_event', motion_hover)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.show()
    return

def plotter (xdata,ydata):
    plt.subplot(122)
    plt.plot(xdata,ydata)
    plt.show()


# asserted_fii_list = pd.read_csv('FII_LIST_ACTIVE.CSV',sep=',')
# asserted_list = pd.read_csv('test.csv',sep=',')

#plotter(asserted_fii_list.pop('DIV'), asserted_fii_list.pop('PVP'),asserted_fii_list.pop('VALUE'),asserted_fii_list.pop('COD'), 'Real state fund', 'DIV', 'PVE')

# plotter(asserted_list.pop('Date'), asserted_list.pop('Close'))


