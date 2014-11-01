__author__ = 'pshort'

#dependencies
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

#ROC curve (uses scikit-learn)

def simple_ROC(true_class, predicted_probabilities, title=None, xlabel=None, ylabel=None, legend_loc='lower right', filename=None):
    """
    takes known classification and probability (generated from a classifier) and displays a ROC curve
    """

    fpr, tpr, _ = roc_curve(true_class, predicted_probabilities, pos_label=1)  # determine false positive, true positive rate

    area_under_curve = auc(fpr, tpr)

    plt.plot(fpr, tpr, 'k--', lw=3, label='Mean ROC Area: %0.2f' % area_under_curve)
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(loc=legend_loc)

    font = {'family': 'normal', 'weight': 'bold', 'size': 22}
    plt.rc('font', **font)

    if not filename:
        plt.show()
    else:
        plt.savefig(filename)
        plt.show()

    return