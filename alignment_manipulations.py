import pandas as pd

def subtract_alignment(df1, df2, parameter, name):
    # Ensure both dataframes contain the same detector type
    detector_types_1 = set(df1['type'].unique())
    detector_types_2 = set(df2['type'].unique())

    common_detectors = detector_types_1.intersection(detector_types_2)
    if not common_detectors:
        raise ValueError("The two DataFrames do not contain any common detector types.")

    results = []

    for detector_type in common_detectors:
        df1_filtered = df1[df1['type'] == detector_type]
        df2_filtered = df2[df2['type'] == detector_type]

        # Determine common columns for merging, excluding the parameter initially
        common_columns = ['type']
        possible_columns = ['wheel', 'station', 'sector', 'superlayer', 'endcap', 'ring', 'chamber', 'layer']
        for col in possible_columns:
            if col in df1_filtered.columns and col in df2_filtered.columns:
                common_columns.append(col)
        
        # Merge dataframes on common columns, include the parameter separately
        df1_filtered = df1_filtered[common_columns + [parameter]]
        df2_filtered = df2_filtered[common_columns + [parameter]]
        
        common_locations = pd.merge(
            df1_filtered,
            df2_filtered,
            on=common_columns,
            suffixes=('_df1', '_df2')
        )
        
        # Subtract the parameter values and create the new column
        common_locations[parameter] = common_locations[f'{parameter}_df1'] - common_locations[f'{parameter}_df2']
        
        # Add a new column to indicate the difference
        common_locations["name"] = name
        
        # Select relevant columns for the result
        result_columns = common_columns + [parameter, "name"]
        results.append(common_locations[result_columns])

    # Combine results into a single dataframe
    result_df = pd.concat(results, ignore_index=True)
    
    # Remove columns that contain only NaNs
    result_df.dropna(how='all', axis=1, inplace=True)

    return result_df