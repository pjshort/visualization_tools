__author__ = 'pshort'

#dependencies
import matplotlib.pyplot as plt

# Two Color Histogram

def two_color_hist(counts1, counts2, label, title=None, xlabel=None, ylabel=None, bins=10, normed=False, color=['purple', 'cyan'], filename=None, **kwargs):
    """
    plots a two-color histogram with counts1, counts2 labelled by label=['class1', 'class2']. Useful for feature comparison
    """
    plt.hist([counts1, counts2], bins=bins, normed=normed, color=color, label=label)
    plt.legend(loc=1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    font = {'family': 'normal', 'weight': 'bold', 'size': 22}
    plt.rc('font', **font)

    if not filename:
        plt.show()
    else:
        plt.savefig(filename)
        plt.show()
    plt.close()

    return


# Simple histogram

def simple_hist(items, color='cyan', xlabel='Features', ylabel='Counts', title='Histogram', width=0.5, bins=10, filename=None):
    """
    creates a single histogram from a list of items input using matplotlib
    """

    plt.hist(items, bins, width=width, align='center', color=color)
    plt.xticks(bins, counts.keys())
    plt.ylim(0, max(counts.values()) + 1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    font = {'family': 'normal', 'weight': 'bold', 'size': 22}
    plt.rc('font', **font)

    if not filename:
        plt.show()
    else:
        plt.savefig(filename)
        plt.show()

    plt.close()
    return
