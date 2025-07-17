import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set_style("whitegrid")
sns.set_theme(palette="bright")


def plot_histograms_with_kde(df, cols, hue_col, n_cols=3, figsize=(12, 8)):
    n_rows = (len(cols) + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    axes = axes.ravel()

    for idx, col in enumerate(cols):
        sns.histplot(data=df, x=col, ax=axes[idx], kde=True, hue=hue_col)
        mean = df[col].mean()
        std = df[col].std()
        axes[idx].set_title(f'{col} (μ={mean:.2f}, σ={std:.2f})')

    for j in range(len(cols), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()


def plot_violinplots(df, cols, x_col, n_cols=3, figsize=(12, 8)):
    n_rows = (len(cols) + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    axes = axes.ravel()

    for idx, col in enumerate(cols):
        sns.violinplot(data=df, x=x_col, y=col, ax=axes[idx], inner='quartile', palette='Set2')
        mean = df[col].mean()
        std = df[col].std()
        axes[idx].set_title(f'{col} (μ={mean:.2f}, σ={std:.2f})')
        axes[idx].set_xlabel(x_col)
        axes[idx].set_ylabel(col)

    for j in range(len(cols), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()


def plot_boxplots(df, cols, group_col, n_cols=3, figsize=(12, 8)):
    n_rows = (len(cols) + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    axes = axes.ravel()

    for idx, col in enumerate(cols):
        sns.boxplot(data=df, x=col, ax=axes[idx], hue=group_col)
        axes[idx].set_title(f'Boxplot de {col} por {group_col}')
        if axes[idx].get_legend() is not None:
            axes[idx].legend_.remove()

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=len(labels), fontsize='small', title=group_col)

    for j in range(len(cols), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()


def plot_bar_proportions(df, x_col, group_col=None, title='', xlabel='', ylabel='Proporção', figsize=(12, 8)):
    plt.figure(figsize=figsize)

    if group_col:
        data = (
            df.groupby([x_col, group_col]).size()
            .div(len(df))
            .unstack(fill_value=0)
        )
        ax = data.plot(kind='bar', stacked=False, ax=plt.gca())
    else:
        data = df[x_col].value_counts(normalize=True)
        ax = data.plot(kind='bar', ax=plt.gca())

    plt.title(title)
    plt.xlabel(xlabel or x_col)
    plt.ylabel(ylabel)

    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f"{height:.2%}", (p.get_x() + p.get_width() / 2, height), ha='center', va='bottom', fontweight='bold')

    plt.ylim(0, data.values.max() * 1.15)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.tight_layout()
    plt.show()


def plot_correlation_matrix(df, cols, figsize=(12, 8)):
    corr_matrix = df[cols].corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    plt.figure(figsize=figsize)
    sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", square=True, vmin=-1, vmax=1)
    plt.title("Matriz de Correlação")
    plt.tight_layout()
    plt.show()
