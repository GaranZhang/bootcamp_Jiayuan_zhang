## Project: Seagate Stock Price 

This orchestration plan frames the end-to-end workflow for predicting Seagate stock prices using `yfinance` for data ingestion, feature engineering, model training, and risk communication. The goal is to make the workflow reproducible, traceable, and modular, while identifying which steps should be automated.

## 1. Key Tasks (Lifecycle-Oriented)

Based on the lifecycle framework (see course modules), the project can be broken down into 7 main tasks:

1. **Data Ingestion**  
   - Pull Seagate historical stock data from `yfinance`.  
   - Save raw data to `/data/raw/seagate.csv`.

2. **Data Cleaning & Preprocessing**  
   - Handle missing values, adjust for stock splits/dividends.  
   - Generate cleaned dataset `/data/processed/STX_prices_clean.csv`.

3. **Feature Engineering**  
   - Create lag features, rolling averages, volatility metrics, etc.  
   - Save engineered features to `/data/features/seagate_features.csv`.

4. **Model Training**  
   - Train a time-series regression or classification model.  
   - Save trained model as `/model/seagate_model.pkl`.

5. **Model Evaluation & Risk Communication**  
   - Compute RMSE, MAPE, and backtest results.  
   - Log results to `/reports/metrics.json`.  
   - Generate stakeholder summary report `/reports/summary.pdf`.

6. **Prediction & API Exposure**  
   - Load model and serve predictions via Flask API (`/predict` endpoint).  
   - Allow batch predictions with input CSV.  
   - Save prediction results to `/reports/predictions.csv`.

7. **Monitoring & Logging**  
   - Collect logs for data ingestion, training, and inference.  
   - Checkpoint outputs at each stage to support retry and idempotency.


## 2. DAG & Dependencies

**Dependency Flow:**
[Ingest] → [Clean] → [Feature Engineering] → [Model Training] → [Evaluation]→[Prediction & API Serving]


- **Parallelizable tasks:**  
  - Feature engineering can be run in parallel with some exploratory analysis.  
  - Evaluation and reporting can be batched independently after model training.

## 3. Task-Level Details

Task-Level Details (Paragraph Form)

Data Ingestion: The data is retrieved using the yfinance API, with the output saved as /data/raw/STX_prices_20250820-234954.csv. This step is idempotent (the same date range always produces the same output). Logs are written to logs/ingestion.log, and the raw file is stored as a checkpoint.

Data Cleaning: The input is /data/raw/STX_prices_20250820-234954.csv, and the output is /data/processed/STX_prices_clean_20250821-002216.csv. This step is idempotent since deterministic cleaning rules are applied. Logs are stored in src/cleaning.py, and the cleaned dataset is saved as a checkpoint.

Feature Engineering: The input is /data/raw/STX_prices_20250820-234954.csv, and the output is /data/processed/seagate_features.csv. This step is idempotent, with logs written to src/features.py, and the feature file stored as a checkpoint.

Model Training: The input is /data/features/seagate_features.csv. This step is not strictly idempotent because random seeds can cause variation unless fixed. Logs are stored and the model file is saved as a checkpoint.

Model Evaluation:This step is idempotent given a fixed data split and seed. Logs are written and evaluation metrics are stored as a checkpoint.

Prediction & API: This step is idempotent, with logs recorded and predictions stored as a checkpoint.

Monitoring: This step aggregates logs from all tasks to produce alerts or dashboards. Since there is no direct file input/output, idempotency does not apply. Logs are collected centrally, and monitoring metrics are stored in a database.

## 4. Failure Points & Retry Policy

- **Data Ingestion:** Failure if API request fails (retry with exponential backoff, up to 3 attempts).  
- **Data Cleaning:** Failure if missing critical columns (halt, require manual check).  
- **Feature Engineering:** Failure if transformations generate NaN (log and drop affected rows).  
- **Model Training:** Failure if convergence error (retry with adjusted hyperparameters).  
- **API Serving:** Failure if endpoint down (restart again).

## 5. Automation Strategy

- **Automate Now:**  
  - Data ingestion, cleaning, feature engineering → can be fully scripted and run daily via cron/airflow.  
  - Model training and evaluation → can be automated but with fixed seeds to ensure reproducibility.  
  - Logging and checkpoints → essential for reproducibility.

- **Keep Manual for Now:**  
  - Hyperparameter tuning (still exploratory due to my ability right now).  
  - Stakeholder reporting (summary PDF generation requires narrative input). 
  - Deployment monitoring dashboards (manual setup until scale justifies automation).

## 6. Logging & Checkpoint Strategy

- **Centralized logs:** All steps log to `/logs/*.log` with timestamps, errors, and warnings.  
- **Checkpoints:** Each step saves outputs in structured folders (`/data/raw`, `/data/processed`).  
- **Recovery:** Any step can be re-run from last valid checkpoint without re-running the entire pipeline.

## Conclusion

This orchestration plan ensures the Seagate stock prediction project is modular, reproducible, and partially automatable. The DAG structure highlights dependencies while leaving room for parallelization. Automated checkpoints and retry strategies enhance reliability, while manual review remains for critical outputs like reports and strategic decisions.


