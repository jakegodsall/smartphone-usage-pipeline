# Smartphone Usage Pipeline

An end-to-end machine learning pipeline for predicting smartphone usage and addiction, built with AWS SageMaker Pipelines.

> **Note:** This project is for learning purposes only.

---

## Overview

This project implements a supervised regression pipeline trained on the open-source Kaggle dataset [Smartphone Usage & Addiction Prediction](https://www.kaggle.com/datasets/jayjoshi37/smartphone-usage-and-addiction-prediction). The pipeline covers data preprocessing, model training, evaluation, and deployment (orchestrated using AWS SageMaker Pipelines).

## Pipeline Architecture

```
Raw Data (Kaggle)
    │
Preprocessing Step        # Feature engineering, encoding, scaling
    │
Training Step             # Regression model training on SageMaker
    │
Evaluation Step           # Compute metrics (RMSE, R², etc.)
    │
Model Registration        # Conditional registration to Model Registry
    │
Deployment                # SageMaker endpoint
```

## Tech Stack

| Layer | Technology |
|---|---|
| Pipeline orchestration | AWS SageMaker Pipelines |
| Model training | scikit-learn / XGBoost |
| Data processing | pandas, numpy |
| Infrastructure | AWS S3, IAM, SageMaker |
| Language | Python 3.10+ |

## Dataset

**Source:** [Kaggle: Smartphone Usage & Addiction Prediction](https://www.kaggle.com/datasets/jayjoshi37/smartphone-usage-and-addiction-prediction)

The dataset contains features related to smartphone behaviour (screen time, app usage, notifications, etc.) with a target variable for addiction/usage intensity.
