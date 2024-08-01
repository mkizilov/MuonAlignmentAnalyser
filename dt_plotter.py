import matplotlib.pyplot as plt

def plot_DT_chamber_alignment(dfs, wheel, station, sector, par, saveplot=False):
    if not isinstance(dfs, list):
        dfs = [dfs]
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # List of colors to use for different DataFrames
    plt.figure(figsize=(15, 5))
    
    for i, df in enumerate(dfs):
        df_filtered = df[(df['wheel'] == wheel) & (df['station'] == station) & (df['type'] == 'DTChamber')]
        filename = df_filtered['name'].unique()[0]
        color = colors[i % len(colors)]  # Cycle through the list of colors
        
        plt.scatter(df_filtered['sector'], df_filtered[par], c=color, label=filename)

    # Draw vertical lines to separate superlayers
    for sector in df_filtered['sector'].unique():
        plt.axvline(sector, color='grey', linestyle='--', linewidth=0.5)
        
    # Set superlayer xticks
    plt.xticks(df_filtered['sector'].unique(), labels=df_filtered['sector'].unique())

    plt.legend()
    plt.xlabel('DT Chamber')
    plt.ylabel(par + ' [cm] or [rad]')
    plt.title(f'Parameter {par} for Wheel {wheel}, Station {station}')
    
    # Save plot
    if saveplot:
        plt.tight_layout()
        plt.savefig(f'plots/{saveplot}.png')
    
    plt.show()
    
def plot_DT_layer_alignment(dfs, wheel, station, sector, superlayer, par, saveplot=False):
    if not isinstance(dfs, list):
        dfs = [dfs]
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # List of colors to use for different DataFrames
    plt.figure(figsize=(15, 5))


    for i, df in enumerate(dfs):

        df_filtered = df[(df['wheel'] == wheel) & (df['station'] == station) & (df['sector'] == sector) & (df['superlayer'] == superlayer) & (df['type'] == 'DTLayer')]
        filename = df_filtered['name'].unique()[0]
        color = colors[i % len(colors)]  # Cycle through the list of colors
        
        plt.scatter(df_filtered['layer'], df_filtered[par], c=color, label=filename)

    # Draw vertical lines to separate layers
    for layer in df_filtered['layer'].unique():
        plt.axvline(layer, color='grey', linestyle='--', linewidth=0.5)
        
    # Set layer xticks
    plt.xticks(df_filtered['layer'].unique(), labels=df_filtered['layer'].unique())

    plt.legend()
    plt.xlabel('DT Layer')
    plt.ylabel(par + ' [cm] or [rad]')
    plt.title(f'Parameter {par} for Wheel {wheel}, Station {station}, Sector {sector}, Superlayer {superlayer}')
    
    # Save plot
    if saveplot:
        plt.tight_layout()
        plt.savefig(f'plots/{saveplot}.png')
    plt.show()

def plot_DT_superlayer_alignment(dfs, wheel, station, sector, par, saveplot=False):
    if not isinstance(dfs, list):
        dfs = [dfs] 
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # List of colors to use for different DataFrames
    plt.figure(figsize=(15, 5))
    
    for i, df in enumerate(dfs):
        df_filtered = df[(df['wheel'] == wheel) & (df['station'] == station) & (df['sector'] == sector) & (df['type'] == 'DTSuperLayer')]
        filename = df_filtered['name'].unique()[0]
        color = colors[i % len(colors)]
        plt.scatter(df_filtered['superlayer'], df_filtered[par], c=color, label=filename)
        
    # Draw vertical lines to separate superlayers
    for superlayer in df_filtered['superlayer'].unique():
        plt.axvline(superlayer, color='grey', linestyle='--', linewidth=0.5)
        
    # Set superlayer xticks
    plt.xticks(df_filtered['superlayer'].unique(), labels=df_filtered['superlayer'].unique())
    
    plt.legend()
    plt.xlabel('DT SuperLayer')
    plt.ylabel(par + ' [cm] or [rad]')
    plt.title(f'Parameter {par} for Wheel {wheel}, Station {station}, Sector {sector}')
    
    # Save plot
    if saveplot:
        plt.tight_layout()
        plt.savefig(f'plots/{saveplot}.png')
        
    plt.show()