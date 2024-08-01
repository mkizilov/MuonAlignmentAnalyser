import matplotlib.pyplot as plt
import ROOT
import uproot
import pandas as pd
from matplotlib.colors import LogNorm #For log scale colorbars
import numpy as np
from scipy.optimize import curve_fit

def plot_CSC_chambers_alignment(dfs, endcap, station, ring, par, saveplot=False):
    if not isinstance(dfs, list):
        dfs = [dfs]
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # List of colors to use for different DataFrames
    plt.figure(figsize=(15, 5))
    
    for i, df in enumerate(dfs):
        df_filtered = df[(df['endcap'] == endcap) & (df['station'] == station) & (df['ring'] == ring) & (df['type'] == 'CSCChamber')]
        filename = df_filtered['name'].unique()[0]
        color = colors[i % len(colors)]  # Cycle through the list of colors
        
        plt.scatter(df_filtered['chamber'], df_filtered[par], c=color, label=filename, alpha=0.5, s=50)

    # Draw vertical lines to separate chambers
    for chamber in df_filtered['chamber'].unique():
        plt.axvline(chamber, color='grey', linestyle='--', linewidth=0.5)
        
    # Set chamber xticks
    plt.xticks(df_filtered['chamber'].unique(), labels=df_filtered['chamber'].unique())

    plt.legend()
    plt.xlabel('CSC Chamber')
    plt.ylabel(par + ' [cm] or [rad]')
    plt.title(f'Parameter {par} for Endcap {endcap}, Station {station}, Ring {ring}')
    
    # Save plot
    if saveplot:
        plt.tight_layout()
        plt.savefig(f'plots/{saveplot}.png')
    
    plt.show()
    
def plot_CSC_layer_alignment(df_list, endcap, station, ring, chamber, parameter, saveplot=False, df_list_chamber=None):
    if not isinstance(df_list, list):
        df_list = [df_list]
    if df_list_chamber is not None:
        chamber_line = True
    if not isinstance(df_list_chamber, list) and df_list_chamber is not None:
        df_list_chamber = [df_list_chamber]
    colors = ['red', 'blue', 'green', 'grey', 'black', 'yellow', 'orange']
    markers = ['o', 's', 'D', '^', 'v', '>', '<']
    
    plt.figure(figsize=(5, 10))
    
    for i, df in enumerate(df_list):
        # Filter dataframe based on the provided endcap, station, ring, and chamber
        df_filtered = df[(df['endcap'] == endcap) & (df['station'] == station) & (df['ring'] == ring) & (df['chamber'] == chamber)]
        
        # Check if the parameter exists in the dataframe
        if parameter not in df_filtered.columns:
            print(f"The parameter '{parameter}' does not exist in the dataframe corresponding to the XML file '{df['name'].iloc[0]}'.")
            continue
        
        # Sort the dataframe by 'layer'
        df_filtered['layer'] = df_filtered['layer'].astype(int)
        df_filtered = df_filtered.sort_values(by='layer')

        # Scatter plot the data
        plt.scatter(df_filtered['layer'], df_filtered[parameter] * 10000, label=df['name'].iloc[0], marker=markers[i % len(markers)], color=colors[i % len(colors)], linewidths=3)
    
    # Plot horizontal chamber line if chamber data is provided
    if df_list_chamber:
        for i, df in enumerate(df_list_chamber):
            if chamber_line and df_list_chamber:
                df_chamber_filtered = df_list_chamber[i][(df_list_chamber[i]['endcap'] == endcap) & (df_list_chamber[i]['station'] == station) & (df_list_chamber[i]['ring'] == ring) & (df_list_chamber[i]['chamber'] == chamber)]
                if not df_chamber_filtered.empty:
                    plt.axhline(y=df_chamber_filtered[parameter].values[0] * 10000, color=colors[i % len(colors)], linestyle='--', label = df_list_chamber[i]['name'].iloc[0])
    # Add vertical lines for each layer
    for k in range(1, 7):
        plt.axvline(x=k, color="grey", linestyle='dotted', linewidth=0.5)
    
    # Add labels and title
    plt.xlabel('Layer Number')
    plt.ylabel(f'{parameter} [µm]')
    plt.title(f'Plot of {parameter} by layer number for endcap {endcap}, station {station}, ring {ring}, and chamber {chamber}')
    
    # Add a legend
    plt.legend()

    # Save the plot if required
    if saveplot:
        plt.tight_layout()
        plt.savefig(f'plots/{saveplot}.png')
    
    # Show the plot
    plt.show()
    
def select_layer(df, endcap=None, station=None, ring=None, chamber=None, layer=None):
    df_filtered = df.copy()
    if endcap is not None:
        df_filtered = df_filtered[df_filtered['prop_location[0]'] == endcap]
    if station is not None:
        df_filtered = df_filtered[df_filtered['prop_location[1]'] == station]
    if ring is not None:
        df_filtered = df_filtered[df_filtered['prop_location[2]'] == ring]
    if chamber is not None:
        df_filtered = df_filtered[df_filtered['prop_location[3]'] == chamber]
    if layer is not None:
        df_filtered = df_filtered[df_filtered['prop_location[4]'] == layer]
    return df_filtered

def plot_RdPhi_fit(df, endcap=None, station=None, ring=None, chamber=None, layer=None, hist_range=(-2, 2), bins=100):
    df_filtered = select_layer(df, endcap, station, ring, chamber, layer)

    if df_filtered.empty:
        print("No data found for the specified filters.")
        return

    plot_name = df_filtered['name'].iloc[0]

    # Calculate statistics
    mean = df_filtered['RdPhi'].mean()
    std = df_filtered['RdPhi'].std()
    n_entries = len(df_filtered)

    # Plot the histogram
    hist, bin_edges = np.histogram(df_filtered['RdPhi'], bins=bins, range=hist_range)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    plt.hist(df_filtered['RdPhi'], bins=bins, range=hist_range, alpha=0.7, label=plot_name)

    # Define the single Gaussian function
    def single_gaussian(x, A, mu, sigma):
            return A * np.exp(-(x - mu)**2 / (2 * sigma**2))

    # Initial guess for parameters of the Gaussian
    A_initial = hist.max()
    p0 = [A_initial, mean, std]

    try:
        popt, _ = curve_fit(single_gaussian, bin_centers, hist, p0=p0, maxfev=10000)
    except RuntimeError as e:
        print(f"Fit failed: {e}")
        return

    # Plot the Gaussian fit
    x_fit = np.linspace(hist_range[0], hist_range[1], 1000)
    y_fit = single_gaussian(x_fit, *popt)
    plt.plot(x_fit, y_fit, 'r-', label='Gaussian Fit')

    # Set labels and title
    plt.xlabel('RdPhi [cm]')
    plt.ylabel('Entries')
    plt.title(f'endcap {endcap}, station {station}, ring {ring}, chamber {chamber}, layer {layer}')

    # Display statistics
    mean_fit, std_fit = popt[1], popt[2]
    plt.text(0.7, 0.5, f'Mean: {mean_fit:.2f}\nSTD: {std_fit:.2f}\nEntries: {n_entries}', transform=plt.gca().transAxes)

    # Add legend
    plt.legend()

    plt.show()
    
def plot_entries_heatmap(df, endcap=None, station=None, ring=None, chamber=None, layer=None):
    data = select_layer(df, endcap, station, ring, chamber, layer)
    plot_name = data['name'].iloc[0]
    hist, xedges, yedges = np.histogram2d(data["prop_GP[0]"], data["prop_GP[1]"], bins=(200, 200))
    hist[hist == 0] = np.nan
    plt.imshow(hist.T, extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap='viridis', origin='lower', vmin=1)
    plt.title(f"CSC Propagation Global endcap {endcap}" + f" station {station}" + f" ring {ring}" + f" chamber {chamber}" + f" layer {layer} " + plot_name)
    plt.xlabel("prop x [cm]")
    plt.ylabel("prop y [cm]")
    plt.colorbar()
    plt.show()
    plt.close()
    
def plot_RdPhi_heatmap(df, endcap = None, station = None, ring = None, chamber = None, layer = None):
    df = select_layer(df, endcap, station, ring, chamber, layer)
    # df = df[(df['muon_pt'] > 10) & (df['muon_pt'] < 30) & (df['muon_charge'] ==-1)]
    max_i = df['prop_location[3]'].max()
    max_j = df['prop_location[4]'].max()

    layer_x = df['prop_GP[0]'].values
    layer_y = df['prop_GP[1]'].values
    layer_RdPhi = df['RdPhi'].values

    # Create a 2D histogram with specified number of bins
    bins_x = np.linspace(layer_x.min(), layer_x.max(), 100)  # Adjust the number of bins as needed
    bins_y = np.linspace(layer_y.min(), layer_y.max(), 100)  # Adjust the number of bins as needed
    hist, x_edges, y_edges = np.histogram2d(layer_x, layer_y, bins=[bins_x, bins_y], weights=layer_RdPhi)

    # Calculate the mean RdPhi values within each bin
    hist_counts, _, _ = np.histogram2d(layer_x, layer_y, bins=[bins_x, bins_y])
    hist_mean = np.divide(hist, hist_counts, where=hist_counts != 0)

    # Create a colormap and plot the 2D histogram using mean RdPhi values as colors
    plt.imshow(hist_mean.T, extent=[x_edges.min(), x_edges.max(), y_edges.min(), y_edges.max()], origin='lower', cmap='seismic', aspect='auto', vmin=-np.max(np.abs(hist_mean)), vmax=np.max(np.abs(hist_mean)))
    cbar = plt.colorbar()
    cbar.set_label('RdPhi [cm]')
    # Fill empty space with light grey
    plt.xlabel('X [cm]')
    plt.ylabel('Y [cm]')
    plt.title(f'endcap {endcap}')

    plt.show()