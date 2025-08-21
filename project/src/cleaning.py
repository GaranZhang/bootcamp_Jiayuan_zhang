import pandas as pd
import numpy as np

def fill_missing_median(df: pd.DataFrame, cols: list) -> pd.DataFrame:
 
    for col in cols:
        if col in df.columns:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
    return df


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    row_thresh = int((1 - threshold) * df.shape[1])
    return df.dropna(thresh=row_thresh)


def normalize_data(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    for col in cols:
        if col in df.columns:
            min_val = df[col].min()
            max_val = df[col].max()
            if max_val > min_val:  # avoid division by zero
                df[col] = (df[col] - min_val) / (max_val - min_val)
    return df
