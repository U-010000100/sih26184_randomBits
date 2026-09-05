import joblib
import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split

# Step 1: Feature Engineering
def extract_features(df_logs):
    df = df_logs.copy()

    # Temporal Features
    df["hour_of_day"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek

    # Spatial Risk Aggregations (Historical velocity per H3 Cell)
    h3_counts = df.groupby("h3_cell_id")["transaction_id"].transform("count")
    df["h3_transaction_velocity"] = h3_counts

    # Mock Graph Centrality (Degrees of mule accounts)
    mule_degrees = df.groupby("target_account")["source_account"].transform(
        "nunique"
    )
    df["mule_graph_degree"] = mule_degrees

    # Categorical Conversions for LightGBM
    df["h3_cell_id"] = df["h3_cell_id"].astype("category")
    df["terminal_type"] = df["terminal_type"].astype("category")

    feature_cols = [
        "amount",
        "hour_of_day",
        "day_of_week",
        "h3_transaction_velocity",
        "mule_graph_degree",
        "h3_cell_id",
        "terminal_type",
    ]

    X = df[feature_cols]
    y = df["is_fraud_cashout"]

    return X, y


# Step 2: Model Training and Evaluation Pipeline
def train_predictive_model(X, y):
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # LightGBM Dataset conversion
    train_data = lgb.Dataset(X_train, label=y_train)
    valid_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

    # Model Parameters tailored for Imbalanced Fraud Detection
    params = {
        "objective": "binary",
        "metric": "auc",
        "boosting_type": "gbdt",
        "is_unbalance": True,  # Optimizes recall for imbalanced fraud events
        "learning_rate": 0.05,
        "num_leaves": 31,
        "verbose": -1,
        "random_state": 42,
    }

    # Model Training
    model = lgb.train(
        params,
        train_data,
        num_boost_round=100,
        valid_sets=[valid_data],
    )

    # Inference & Evaluation
    risk_scores = model.predict(X_test)
    y_pred = (risk_scores > 0.5).astype(int)

    print("\n--- Model Evaluation ---")
    print(f"ROC-AUC Score: {roc_auc_score(y_test, risk_scores):.4f}")
    print(classification_report(y_test, y_pred))

    # Save trained model artifact for FastAPI serving
    joblib.dump(model, "lightgbm_cashout_model.pkl")
    print("Model serialized and saved as 'lightgbm_cashout_model.pkl'")


if __name__ == "__main__":
    # Load logs generated in Phase 1
    df_logs = pd.read_csv("transaction_logs.csv")
    df_logs["timestamp"] = pd.to_datetime(df_logs["timestamp"])

    # Execute Phase 2 Pipeline
    X, y = extract_features(df_logs)
    train_predictive_model(X, y)