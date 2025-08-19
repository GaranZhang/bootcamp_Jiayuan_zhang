import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df, cols):
    """Fill missing values in the given columns with their median."""
    for col in cols:
        if col in df.columns:
            median = df[col].median()
            df[col] = df[col].fillna(median)
    return df


def drop_missing(df, threshold=0.5):
    """Drop rows with too many missing values (ratio above threshold)."""
    return df.dropna(thresh=int((1 - threshold) * df.shape[1]))


def normalize_data(df, cols):
    """Normalize numerical columns to [0,1] using MinMaxScaler."""
    scaler = MinMaxScaler()
    for col in cols:
        if col in df.columns:
            df[col] = scaler.fit_transform(df[[col]])
    return df
