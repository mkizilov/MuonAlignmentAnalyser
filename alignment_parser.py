import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np
import os
import uproot

def parse_xml_alignment(file_path, detector_type, name=None):
    # Extract the filename from the file path
    filename = os.path.basename(file_path)
    
    # Use provided name or default to filename
    entry_name = name if name else filename
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    
    for operation in root.findall('operation'):
        for child in operation:
            if child.tag.startswith(detector_type):
                detector = child.tag
                attributes = child.attrib
                
                setposition = operation.find('setposition')
                setape = operation.find('setape')
                
                entry = {
                    'type': detector,
                    'wheel': np.nan, 'station': np.nan, 'sector': np.nan,
                    'superlayer': np.nan, 'endcap': np.nan, 'ring': np.nan, 
                    'chamber': np.nan, 'layer': np.nan,
                    'x': float(setposition.attrib['x']),
                    'y': float(setposition.attrib['y']),
                    'z': float(setposition.attrib['z']),
                    'phix': float(setposition.attrib['phix']),
                    'phiy': float(setposition.attrib['phiy']),
                    'phiz': float(setposition.attrib['phiz']),
                    'xx': float(setape.attrib['xx']),
                    'xy': float(setape.attrib['xy']),
                    'xz': float(setape.attrib['xz']),
                    'xa': float(setape.attrib['xa']),
                    'xb': float(setape.attrib['xb']),
                    'xc': float(setape.attrib['xc']),
                    'yy': float(setape.attrib['yy']),
                    'yz': float(setape.attrib['yz']),
                    'ya': float(setape.attrib['ya']),
                    'yb': float(setape.attrib['yb']),
                    'yc': float(setape.attrib['yc']),
                    'zz': float(setape.attrib['zz']),
                    'za': float(setape.attrib['za']),
                    'zb': float(setape.attrib['zb']),
                    'zc': float(setape.attrib['zc']),
                    'aa': float(setape.attrib['aa']),
                    'ab': float(setape.attrib['ab']),
                    'ac': float(setape.attrib['ac']),
                    'bb': float(setape.attrib['bb']),
                    'bc': float(setape.attrib['bc']),
                    'cc': float(setape.attrib['cc']),
                    'name': entry_name  # Use the provided name or filename
                }
                
                for k, v in attributes.items():
                    if v.lstrip('-').replace('.', '', 1).isdigit():
                        entry[k] = int(v) if v.lstrip('-').isdigit() else float(v)
                    else:
                        entry[k] = np.nan
                
                data.append(entry)
    
    df = pd.DataFrame(data)
    
    # Remove columns that contain only NaNs
    df.dropna(axis=1, how='all', inplace=True)
    
    # Convert detector coordinate columns to integers where applicable
    int_columns = ['wheel', 'station', 'sector', 'superlayer', 'endcap', 'ring', 'chamber', 'layer']
    for col in int_columns:
        if col in df.columns:
            df[col] = df[col].astype(pd.Int64Dtype())
    
    return df

def parse_csv_to_dataframe(file_path, name="CSC Layer Alignment"):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, header=None, names=['detectorId', 'x', 'y', 'z', 'phix', 'phiy', 'phiz', 'numEvents'])

    # Calculate endcap, station, ring, chamber, and layer from detectorId
    df['endcap'] = df['detectorId'].apply(lambda x: 1 if x > 0 else 2)
    df['chamber'] = df['detectorId'].apply(lambda x: abs(x) % 1000 // 10)  # Extract chamber correctly
    df['layer'] = df['detectorId'].apply(lambda x: abs(x) % 10)
    df['station'] = 1  # Assuming station is always 1
    df['ring'] = 1     # Assuming ring is always 1

    # Convert relevant columns to numeric
    df['endcap'] = pd.to_numeric(df['endcap'])
    df['station'] = pd.to_numeric(df['station'])
    df['ring'] = pd.to_numeric(df['ring'])
    df['chamber'] = pd.to_numeric(df['chamber'])
    df['layer'] = pd.to_numeric(df['layer'])
    df['x'] = pd.to_numeric(df['x'])
    df['y'] = pd.to_numeric(df['y'])
    df['z'] = pd.to_numeric(df['z'])
    df['phix'] = pd.to_numeric(df['phix'])
    df['phiy'] = pd.to_numeric(df['phiy'])
    df['phiz'] = pd.to_numeric(df['phiz'])
    df['numEvents'] = pd.to_numeric(df['numEvents'])

    # Adding a column to specify the detector type and name of the alignment
    df['type'] = 'CSCLayer'
    df['name'] = name

    # Rearrange the columns to match the specified order
    df = df[['endcap', 'station', 'ring', 'chamber', 'layer', 'x', 'y', 'z', 'phix', 'phiy', 'phiz', 'numEvents', 'type', 'name']]
    
    return df

def parse_CSC_layer_alignment_root_to_dataframe(file, name = None):
    dataframes = {}
    file = uproot.open(file)
    for key in file.keys():
        if isinstance(file[key], uproot.behaviors.TTree.TTree):
            tree = file[key]
            df = tree.arrays(library="pd")
            dataframes[key] = df
            key_str = key
    dataframes = dataframes[key_str]
    if name is None:
        dataframes['name'] = 'CSCLayerAlignment'
    else:
        dataframes['name'] = name
    return dataframes

def parse_csc_reports(file_path, name=None):
    # Dictionary to store the global namespace
    namespace = {
        'reports': [],
        'ValErr': None,
        'Report': None
    }

    # Define a safe ValErr class
    class ValErr:
        def __init__(self, value, error, antisym):
            self.value = value
            self.error = error
            self.antisym = antisym

    # Define a safe Report class that mimics the original for data storage
    class Report:
        def __init__(self, chamberId, postal_address, name):
            self.chamberId = chamberId
            self.postal_address = postal_address
            self.name = name
            self.posNum = 0
            self.negNum = 0
            self.fittype = None
            self.CovMatrix = None

        def add_parameters(self, deltax, deltay, deltaz, deltaphix, deltaphiy, deltaphiz, loglikelihood, numsegments, sumofweights, redchi2):
            self.deltax = deltax
            self.deltay = deltay
            self.deltaz = deltaz
            self.deltaphix = deltaphix
            self.deltaphiy = deltaphiy
            self.deltaphiz = deltaphiz
            self.loglikelihood = loglikelihood
            self.numsegments = numsegments
            self.sumofweights = sumofweights
            self.redchi2 = redchi2

        def add_stats(self, *args):
            self.stats = args

        def __repr__(self):
            return f"<Report {self.name}>"

    # Inject our safe Report and ValErr classes into the namespace
    namespace['Report'] = Report
    namespace['ValErr'] = ValErr

    # Read and execute the Python file content safely
    with open(file_path, 'r') as file:
        exec(file.read(), namespace)

    # Extract data from the namespace
    reports = namespace['reports']
    data = []
    for report in reports:
        if report.postal_address[0] == "CSC":
            entry = {
                'chamberId': report.chamberId,
                'endcap': report.postal_address[1],
                'station': report.postal_address[2],
                'ring': report.postal_address[3],
                'chamber': report.postal_address[4],
                'name': report.name,
                'posNum': report.posNum,
                'negNum': report.negNum,
                'fittype': report.fittype,
                'x': getattr(getattr(report, 'deltax', None), 'value', None),
                'y': getattr(getattr(report, 'deltay', None), 'value', None),
                'z': getattr(getattr(report, 'deltaz', None), 'value', None),
                'phix': getattr(getattr(report, 'deltaphix', None), 'value', None),
                'phiy': getattr(getattr(report, 'deltaphiy', None), 'value', None),
                'phiz': getattr(getattr(report, 'deltaphiz', None), 'value', None),
                'loglikelihood': getattr(report, 'loglikelihood', None),
                'numsegments': getattr(report, 'numsegments', None),
                'sumofweights': getattr(report, 'sumofweights', None),
                'redchi2': getattr(report, 'redchi2', None),
                'stats': getattr(report, 'stats', None),
                'covmatrix': getattr(report, 'CovMatrix', None)
            }
            data.append(entry)

    # Convert to DataFrame
    df = pd.DataFrame(data)
    df['type'] = 'CSCChamber'
    df['name'] = name if name else 'report.py'
    return df
