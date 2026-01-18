import pandas as pd

def load_variant_data(file_path):
    """
    Load variant data from a CSV or VCF-like file.
    """
    return pd.read_csv(file_path)

def variant_type_summary(df):
    """
    Count mutation types.
    """
    return df['variant_type'].value_counts()