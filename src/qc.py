import pandas as pd
def basic_qc(df: pd.DataFrame) -> dict:
    """
    Perform basic quality control checks on variant data.
    """
    return {
        "total_variants": len(df),
        "unique_genes": df["gene"].nunique(),
        "missing_values": df.isnull().sum().to_dict()
    }