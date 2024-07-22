import matplotlib.pyplot as plt

def plot_CSC_chambers_alignment(dfs, endcap, station, ring, par, saveplot=False):
    if not isinstance(dfs, list):
        dfs = [dfs]
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # List of colors to use for different DataFrames
    plt.figure(figsize=(15, 5))
    
    for i, df in enumerate(dfs):
        df_filtered = df[(df['endcap'] == endcap) & (df['station'] == station) & (df['ring'] == ring) & (df['type'] == 'CSCChamber')]
        filename = df_filtered['name'].unique()[0]
        color = colors[i % len(colors)]  # Cycle through the list of colors
        
        plt.scatter(df_filtered['chamber'], df_filtered[par], c=color, label=filename)

    # Draw vertical lines to separate chambers
    for chamber in df_filtered['chamber'].unique():
        plt.axvline(chamber, color='grey', linestyle='--', linewidth=0.5)
        
    # Set chamber xticks
    plt.xticks(df_filtered['chamber'].unique(), labels=df_filtered['chamber'].unique())

    plt.legend()
    plt.xlabel('CSC Chamber')
    plt.ylabel(par + ' [cm] or [rad]')
    plt.title(f'Local {par} for Endcap {endcap}, Station {station}, Ring {ring}')
    
    # Save plot
    if saveplot:
        plt.tight_layout()
        plt.savefig(f'plots/{saveplot}.png')
    
    plt.show()