HOMEWORK6 DATA_PROCESS

JIAYUAN ZHANG(GARAN ZHANG)

The dataset `instructor_dirty.csv` was processed with these steps:

 --Converted `price` from string ('$100') to numeric('100').
 --Converted `date_str` to datetime format.
 --Filled missing values in numeric columns with the "median".
 --Dropped rows with too many missing values (threshold = 0.5).
 --Normalized numeric columns (`numeric_col`, `price`) to [0, 1].