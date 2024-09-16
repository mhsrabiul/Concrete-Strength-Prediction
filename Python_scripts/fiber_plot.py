
import math
import matplotlib.pyplot as plt

def plot_fiber_scatter(df_imputed):
    # Set the font for the plot
    plt.rcParams['font.family'] = 'serif'  # This uses a generic serif font

    # Calculate fiber counts
    fiber_counts = df_imputed['Fiber Type'].value_counts()

    # Keep top five fiber types
    top_five_fibers = fiber_counts.head(5).index.tolist()

    # Replace other fiber types with 'Others'
    df_imputed['Fiber Type'] = df_imputed['Fiber Type'].apply(lambda x: x if x in top_five_fibers else 'Others')

    # Determine the number of rows and columns for subplots
    num_plots = len(df_imputed.columns) - 1  # Excluding 'CS (MPa)' column
    num_cols = 3  # Three columns for triple column layout
    num_rows = math.ceil(num_plots / num_cols)

    # Create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(18, 6 * num_rows))

    # Flatten the axes if there is only one row
    if num_rows == 1:
        axes = axes.reshape(1, -1)

    # Iterate over each feature and create scatter plot against 'CS (MPa)'
    for i, (feature, ax) in enumerate(zip(df_imputed.columns[:-1], axes.flatten())):
        for fiber_type in df_imputed['Fiber Type'].unique():
            subset = df_imputed[df_imputed['Fiber Type'] == fiber_type]
            ax.scatter(subset[feature], subset['CS (MPa)'], label=fiber_type)
        ax.set_xlabel(feature, fontsize=18)
        ax.set_ylabel('CS (MPa)', fontsize=18)
        ax.tick_params(axis='both', which='major', labelsize=18)
        ax.legend(fontsize=16)

    # Remove any blank subplots
    for i in range(num_plots, num_rows * num_cols):
        fig.delaxes(axes.flatten()[i])

    plt.tight_layout()
    plt.show()

    #plt.savefig('fiber scattered plot.png', dpi=1000)

    

