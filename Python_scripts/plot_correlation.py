import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(df, selected_features, save_path='corr_plot.png'):
    """
    Function to plot and save a correlation heatmap of selected features from a DataFrame.
    
    Parameters:
    df (pd.DataFrame): The dataset.
    selected_features (list): List of feature names to include in the correlation matrix.
    save_path (str): Path to save the figure (default: 'corr_plot.png').
    """
    
    # Set the font family for the plot
    plt.rcParams['font.family'] = 'serif'

    # Create a subset DataFrame with only the selected features
    subset_df = df[selected_features]

    # Compute the correlation matrix
    corr_matrix = subset_df.corr().round(3)

    # Create a mask to hide the upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)

    # Plot the correlation heatmap with triangular mask
    plt.figure(figsize=(14, 6))  # Adjust the figure size as needed
    sns.heatmap(corr_matrix, annot=True, cmap="crest", mask=mask, cbar=False)
    plt.show()

    # Save the heatmap to the specified file
    plt.savefig(save_path, dpi=600, bbox_inches='tight')
    
