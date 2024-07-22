import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np
import os

def parse_xml_alignment(file_path, detector_type):
    # Extract the filename from the file path
    filename = os.path.basename(file_path)
    
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
                    'name': filename  # Add the filename here
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
