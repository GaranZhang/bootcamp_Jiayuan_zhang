import pandas as pd
import numpy as np
from pathlib import Path


def make_features(df: pd.DataFrame, price_col: str = "price", date_col: str = "date") -> pd.DataFrame:
  
    # === Check columns ===
    if price_col not in df.columns:
        raise ValueError(f"Column '{price_col}' not found in DataFrame.")
    if date_col not in df.columns:
        raise ValueError(f"Column '{date_col}' not found in DataFrame.")

    df = df.copy()

    # === Ensure datetime and sort ===
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(by=date_col).reset_index(drop=True)

    # --- Basic Returns ---
    df["Return"] = df[price_col].pct_change()
    df["LogReturn"] = np.log(df[price_col] / df[price_col].shift(1))
    df["CumReturn"] = (1 + df["Return"]).cumprod() - 1

    # --- Lag Features ---
    for lag in [1, 2, 5]:
        df[f"Return_Lag{lag}"] = df["Return"].shift(lag)

    # --- Moving Averages ---
    for window in [5, 10, 20]:
        df[f"MA_{window}"] = df[price_col].rolling(window).mean()

    # --- Rolling Volatility ---
    for window in [5, 20]:
        df[f"Volatility_{window}"] = df["Return"].rolling(window).std()

    # --- Bollinger Bands (20-day) ---
    mid = df[price_col].rolling(20).mean()
    std = df[price_col].rolling(20).std()
    df["BB_Mid"] = mid
    df["BB_Upper"] = mid + 2 * std
    df["BB_Lower"] = mid - 2 * std

    # --- RSI (14-day) ---
    window = 14
    delta = df[price_col].diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = pd.Series(gain).rolling(window).mean()
    avg_loss = pd.Series(loss).rolling(window).mean()
    rs = avg_gain / (avg_loss + 1e-9)
    df["RSI_14"] = 100 - (100 / (1 + rs))

    return df


def main():
    processed_dir = Path("../data/processed")
    input_file = processed_dir / "seagate_no_outliers.csv"
    output_file = processed_dir / "seagate_features.csv"

    df = pd.read_csv(input_file)
    df = make_features(df, price_col="price", date_col="date")
    df.to_csv(output_file, index=False)
    print(f"Feature-engineered dataset saved to {output_file}")


if __name__ == "__main__":
    main()
