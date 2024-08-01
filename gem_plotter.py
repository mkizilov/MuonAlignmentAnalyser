import matplotlib.pyplot as plt

def plot_GEM_superchamber_alignment(dfs, endcap, station, ring, par, saveplot=False):
    if not isinstance(dfs, list):
        dfs = [dfs]
        
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # List of colors to use for different DataFrames
    plt.figure(figsize=(15, 5))
    
    for i, df in enumerate(dfs):
        df_filtered = df[(df['endcap'] == endcap) & (df['station'] == station) & (df['ring'] == ring) & (df['type'] == 'GEMSuperChamber')]
        filename = df['name'].unique()[0]
        color = colors[i % len(colors)]
        plt.scatter(df_filtered['chamber'], df_filtered[par], c=color, label=filename)
        
    # Draw vertical lines to separate superchambers
    for superchamber in df_filtered['chamber'].unique():
        plt.axvline(superchamber, color='grey', linestyle='--', linewidth=0.5)
        
    # Set superchamber xticks
    plt.xticks(df_filtered['chamber'].unique(), labels=df_filtered['chamber'].unique())
    
    plt.legend()
    plt.xlabel('GEM SuperChamber')
    plt.ylabel(par + ' [cm] or [rad]')
    plt.title(f'Parameter {par} for Endcap {endcap}, Station {station}, Ring {ring}')
    
    # Save plot
    if saveplot:
        plt.tight_layout()
        plt.savefig(f'plots/{saveplot}.png')
        
    plt.show()