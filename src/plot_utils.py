import matplotlib.pyplot as plt
import numpy as np


def plot_umap(embedding, names, delta_font=1e-4, display_title=False):
    plt.scatter(embedding[:, 0], embedding[:, 1])
    plt.xticks([])
    plt.yticks([])
    plt.box(False)

    if display_title:
        plt.title('UMAP projection of Epic Games tags')

    add_labels_to_plot(plt, embedding, names, delta_font)


def add_labels_to_plot(plt, embedding, names, delta_font=1e-4):
    # Add a label to each node. The challenge here is that we want to
    # position the labels to avoid overlap with other labels
    # Reference: http://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html
    for index, (name, (x, y)) in enumerate(zip(names, embedding, strict=True)):
        dx = x - embedding[:, 0]
        dx[index] = 1
        dy = y - embedding[:, 1]
        dy[index] = 1
        this_dx = dx[np.argmin(np.abs(dy))]
        this_dy = dy[np.argmin(np.abs(dx))]
        if this_dx > 0:
            horizontalalignment = "left"
            x_new = x + delta_font
        else:
            horizontalalignment = "right"
            x_new = x - delta_font
        if this_dy > 0:
            verticalalignment = "bottom"
            y_new = y + delta_font
        else:
            verticalalignment = "top"
            y_new = y - delta_font
        plt.text(
            x_new,
            y_new,
            name,
            size=10,
            horizontalalignment=horizontalalignment,
            verticalalignment=verticalalignment,
            bbox={
                'facecolor': "w",
                'alpha': 0.6,
            },
        )

    plt.xlim(
        embedding[:, 0].min() - 10 * delta_font * embedding[:, 0].ptp(),
        embedding[:, 0].max() + 10 * delta_font * embedding[:, 0].ptp(),
    )
    plt.ylim(
        embedding[:, 1].min() - 10 * delta_font * embedding[:, 1].ptp(),
        embedding[:, 1].max() + 10 * delta_font * embedding[:, 1].ptp(),
    )
