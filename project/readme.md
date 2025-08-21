MINI Project Title  
Garan ZHANG (Jiayuan Zhang)
**Stock Price Prediction using Python**  
**Stage:** Problem Framing & Scoping (Stage 01)  
---
## Problem Statement  
The stock market is inherently volatile and influenced by numerous factors, making price movements difficult to predict. However, the ability to reasonably forecast stock prices can provide significant value to investors, analysts, and financial institutions by supporting decision-making and risk management.  
This project aims to build a predictive model using historical stock price data (e.g., open, close, volume) to forecast short-term stock prices. The project will also include data preprocessing, exploratory data analysis, modeling, evaluation, and visualization of results.  (hope it can be finished)
---
## Stakeholder & User  
- **Stakeholders**: Individual investors, financial analysts, research departments, hedge funds  
- **Users**: Retail investors seeking stock trend insights; quantitative researchers incorporating predictive signals into strategies  
---
## Useful Answer & Decision  
- **Type of Answer**: Predictive  
- **Decision Metric**: Error metrics such as RMSE and MAE  
- **Artifact to Deliver**:  
  - Predictive model (baseline regression model; extended time-series models such as ARIMA/LSTM)  
  - Visualization comparing actual vs. predicted stock prices  
---
## Assumptions & Constraints  
- **Assumptions**:  
  - Historical stock price data contains information that can help predict future movements  
  - External shocks (e.g., policy changes, black swan events) are not explicitly modeled  
- **Constraints**:  
  - Data availability depends on open-source APIs (Yahoo Finance)  
  - Data may not reflect real-time conditions  
  - The project will be implemented in a local VSCode environment with lightweight models  
---
## Known Unknowns / Risks  
- Market volatility may limit predictive accuracy, especially for sudden events  
- The model may overfit historical data and fail to generalize  
- Forecasts are for research and educational purposes only, not for financial advice  
---
## Lifecycle Mapping  
- Goal A → Problem Framing & Scoping   
- Goal B → Data Acquisition/Ingestion 
- Goal C → Data Preprocessing & Outlier Analysis 
- Goal D → Feature Engineering & Modeling 
- Goal E → Evaluation & Results Reporting 
---
## Repo Plan
/data/ # Raw and processed datasets
/src/ # Python scripts (data cleaning, feature engineering, modeling)
/notebooks/ # Jupyter notebooks (EDA, experiments, prototyping)
/docs/ # Documentation and reports
README.md # Project description
