
import pandas as pd

def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return (series < lower) | (series > upper)


def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:

    mu = series.mean()
    sigma = series.std(ddof=0)
    if sigma == 0:
        return pd.Series([False] * len(series), index=series.index)
    z = (series - mu) / sigma
    return z.abs() > threshold


def winsorize_series(series: pd.Series, lower: float = 0.05, upper: float = 0.95) -> pd.Series:

    lo = series.quantile(lower)
    hi = series.quantile(upper)
    return series.clip(lower=lo, upper=hi)
