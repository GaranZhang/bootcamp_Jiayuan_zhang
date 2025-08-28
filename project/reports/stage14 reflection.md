## Reflection

**Risks if deployed:**  
Deploying a stock price prediction system in production involves several risks. 
1) **model drift** is a major concern, since financial markets are highly dynamic and historical patterns may not generalize to future data. A model that performs well in backtests may generate misleading signals under new regimes, causing financial loss. 
2) **data quality issues** — delayed feeds, missing values, or erroneous outliers can directly impact predictions. 
3) **system-level risks**, such as latency or downtime during market hours, which can prevent timely execution of trades. Finally, regulatory and compliance risks arise if model-driven decisions fail to meet reporting standards.

**Monitoring metrics across layers:**  
- **Data layer:** Monitor feed freshness (e.g., max lag < 2s), missing data rate, and anomaly counts.  
- **Model layer:** Track rolling prediction accuracy, calibration drift, and feature importance stability. Alert if RMSE > historical baseline by >20%.  
- **System layer:** Monitor API latency (p95 < 250ms), throughput, and error rate (<1%). Trigger on-call if exceeded.  

**Ownership & handoffs:**  
The project requires clear ownership across functions. 
The **Data Engineering team** owns feed reliability and preprocessing pipelines. 
The **ML Engineering team** is responsible for model retraining, validation, and deployment. 
The **Platform team** ensures system reliability, monitoring, and alerts. 
The **Business/Trading team** owns the interpretation of predictions, risk management, and decision-making. Handoff readiness is achieved by documenting assumptions, maintaining versioned models, and ensuring reproducibility with standardized APIs. This division of responsibility reduces single points of failure and ensures accountability across the lifecycle.
