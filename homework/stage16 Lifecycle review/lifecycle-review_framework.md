# Lifecycle Review: Seagate Stock Price Prediction Project

## 1. Problem Framing & Scoping
The financial problem was to predict Seagate’s stock price to support investment decision-making. The main goal was to build a predictive model that balances accuracy and interpretability. Constraints included relying solely on Yahoo Finance data and limited computational resources. We assumed that historical prices and derived features could provide predictive signals despite the inherent randomness of financial markets.

## 2. Tooling Setup
We used Python along with `yfinance`, `pandas`, `scikit-learn`, and `matplotlib`. Jupyter Notebook served as the primary development environment. Version conflicts occasionally arose. These were resolved by pinning library versions and using virtual environments.

## 3. Python Fundamentals
Core Python skills applied included data manipulation (pandas), logging, and file management. Ensuring reproducibility across runs was sometimes difficult. I addressed these gaps by reading documentation and repeated practice. Future work should strengthen code modularization.

## 4. Data Acquisition / Ingestion
Data was retrieved from Yahoo Finance via the `yfinance` API and saved into CSV files. The process was stable and reproducible. API rate limits were occasionally an issue. Logging and checkpointing improved robustness.

## 5. Data Storage
Raw data was stored in `/data/raw`, cleaned data in `/data/processed`. The challenge was maintaining a clear structure. This was solved by defining a consistent file organization. In the future, using a database could enhance scalability.

## 6. Data Preprocessing
Preprocessing steps included missing value imputation, column renaming, and date formatting. Gaps in the time series created challenges. Deterministic rules ensured consistency.

## 7. Outlier Analysis
We identified unusual stock price movements as potential outliers. Distinguishing genuine market shocks from data errors was challenging. Some points were capped or adjusted to reduce volatility influence. Future iterations could use volatility clustering or domain-specific techniques.

## 8. Exploratory Data Analysis (EDA)
We plotted price trends, moving averages, and return distributions. Some correlations were misleading at first. Rolling-window plots and lagged scatterplots clarified patterns. Seasonal decomposition and deeper diagnostics could strengthen future EDA.

## 9. Feature Engineering
Features included moving averages, returns, and lagged prices. The main challenge was avoiding look-ahead bias. Feature usefulness was validated via cross-validation. Future work should incorporate more domain-specific indicators such as RSI or MACD.

## 10. Modeling
We started with linear regression and tested more complex models. Overfitting was a major challenge given limited data. Cross-validation and hyperparameter tuning guided the final model choice. Time series models such as ARIMA or LSTMs could be explored further.

## 11. Evaluation & Risk Communication
Metrics used included RMSE and R². The key risk was overreliance on historical patterns that may not persist. We communicated uncertainty using confidence intervals and scenario analysis. Backtesting with simulated trading strategies would improve robustness.

## 12. Results Reporting & Stakeholder Communication
Results were presented through visualizations and reports, focusing on trends and risks. It was challenging to explain limitations to non-technical stakeholders. Comparative scenario plots improved comprehension. Interactive dashboards could enhance communication next time.

## 13. Productization
We modularized the model pipeline and implemented checkpoints for reproducibility. Since the environment was local-only, scalability was limited. Reliability was supported through logging and clear file outputs.  
( **Because I had almost no prior exposure to productization concepts and practices, this stage was particularly difficult for me. I had to learn how to transition from an experimental setup to a reproducible and maintainable structure.**)

## 14. Deployment & Monitoring
Deployment was simulated rather than full production. Logs were kept, and ideas for monitoring (e.g., drift detection) were proposed. Most performance tracking was manual. Automated alerts and real-time dashboards would strengthen monitoring.

## 15. Orchestration & System Design
Tasks were organized in a linear workflow: ingestion → cleaning → feature engineering → modeling → evaluation. Managing dependencies was a challenge. A strict file structure and checkpoints were used. Workflow tools such as Airflow or Prefect could improve orchestration.

## 16. Lifecycle Review & Reflection
This lifecycle highlighted the importance of structure and documentation. The most difficult stages were **Feature Engineering** and **Productization** — the former due to limited financial domain knowledge, and the latter because I had never worked with productization before. The most rewarding stage was **Evaluation**, where I could directly assess model performance and limitations. In the future, I would define evaluation metrics earlier and put more effort into monitoring systems.

---

## Reflection Prompts

- The most difficult stages were **Feature Engineering** and **Productization**. Feature engineering required avoiding look-ahead bias and financial knowledge, while productization was challenging because it was entirely new to me.  
- The most rewarding stage was **Model Evaluation**, as it demonstrated both strengths and weaknesses of the approach.  
- Choices in **Preprocessing and Feature Engineering** had strong effects on later modeling results.  
- If repeating the project, I would spend more time on **System Design and Monitoring** to make the workflow closer to production standards.  
- The skills I most want to strengthen before the next financial engineering project are **time series modeling** and **productization/workflow orchestration frameworks**.  
