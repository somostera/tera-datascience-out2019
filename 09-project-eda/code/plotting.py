import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools


def multiple_histograms_plot(data, x, hue, density=False, bins=10,
                             alpha=0.5, colors=None, hue_order=None,
                             xticks=None, title=None, xlabel=None, ylabel=None, 
                             figsize=(15, 8), xticklabels=None):
    
    hue_order = hue_order if hue_order is not None else sorted(data[hue].unique())
    colors = colors if colors is not None else sns.color_palette(n_colors=len(hue_order))
    colors_dict = dict(zip(hue_order, colors)) 
    
    plt.figure(figsize=figsize)
    for current_hue in hue_order:
        current_hue_mask = data[hue] == current_hue
        data.loc[current_hue_mask, x].hist(bins=bins, density=density,
                                           alpha=alpha, label=str(current_hue), 
                                           color=colors_dict[current_hue]) 
    
    xlabel = x if xlabel is None else xlabel
    ylabel = (ylabel if ylabel is not None 
                     else 'Density' if density 
                     else 'Frequency')
    
    _title_postfix = ' (normalized)' if density else ''
    title = f'{xlabel} by {hue}{_title_postfix}'
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    
    ax = plt.gca()
    if xticks is not None:
        ax.set_xticks(xticks)
    
    if xticklabels is not None:
        ax.set_xticklabels(xticklabels)
        

def countplot_independent_ylims(df, col, hue, size=5, hue_order=None, title=None):
    g = sns.FacetGrid(df, col=hue, sharey=False, size=size)
    g = g.map(sns.countplot, col, order=hue_order)
    plt.subplots_adjust(top=0.85)
    g.fig.suptitle(title)


def plot_1d_corr_heatmap(corr: pd.Series, annot=True, fmt='.2f', 
                         cmap='coolwarm'):
    max_corr = corr.abs().max()
    heatmap_df = pd.DataFrame(corr.sort_values(ascending=False))
    plt.subplots(figsize=(1.5, len(corr)//3.5))

    sns.heatmap(heatmap_df, annot=annot, fmt=fmt, cmap=cmap,
                center=0, vmin=-max_corr, vmax=max_corr)
