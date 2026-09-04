# Predictive Analytics Framework for Cybercrime Prevention

## 🚨 SIH26184

A predictive analytics platform for **forecasting likely cash-withdrawal locations from cybercrime complaints and transaction patterns**. The system combines large-scale data engineering, graph analytics, geospatial intelligence, machine learning, real-time alerting, and an operational dashboard.

---

## 📌 Problem Overview

Cybercrime complaints contain critical data on fraudulent transactions, victims, routes, timing, and financial behavior.

This project transforms that data into **actionable intelligence** by:

- Processing cybercrime and transaction data at scale
- Detecting entity and transaction relationships
- Performing geospatial analysis
- Predicting high-risk withdrawal locations
- Generating real-time alerts
- Displaying predictions on a command dashboard
- Delivering alerts to relevant stakeholders

---

# 🏗️ System Architecture

The system architecture is structured across seven core layers designed for end-to-end processing:

1. **Data Ingestion & ETL Layer**: Uses **Apache Kafka** for streaming incoming events, **PySpark** for distributed processing, **Apache Airflow** for workflow orchestration, and **PostgreSQL** for relational storage.
2. **Graph Database Layer**: Employs **Neo4j** for structured graph storage and relationship querying, paired with **PyTorch Geometric** for deep learning on graph topologies.
3. **Geospatial Indexing Layer**: Combines **PostGIS** for storing spatial geometries with **Uber H3** for hierarchical hexagonal indexing.
4. **Predictive AI / ML Core**: Leverages **LightGBM**, **Pandas**, **NumPy**, and **Scikit-learn** in **Python** to handle feature engineering, model training, risk prediction, and ranking.
5. **Real-Time Alert Engine**: Powered by **FastAPI** as the gateway, **Redis** for caching/queuing, **Celery** for asynchronous job execution, and APIs like **Twilio** and **Firebase Cloud Messaging (FCM)** for delivery.
6. **LEA Command Dashboard**: A web interface built with **React.js**, **Tailwind CSS**, **Mapbox GL JS**, and **Deck.gl** to visualize risk scores, real-time alerts, and historical data.
7. **Mobile Alerting Layer**: A mobile application built with **React Native**, **PWA**, and **Firebase Cloud Messaging (FCM)** to deliver push alerts directly to personnel in the field.

---

# 🤖 Machine Learning Workflow

The ML pipeline converts historical cybercrime and transaction data into **ranked predictions of likely withdrawal locations**:

1. **Data Preprocessing**: Ingests raw historical transactions and cybercrime complaints, performing cleaning and normalization using **Pandas** and **NumPy**.
2. **Feature Engineering**: Generates multi-dimensional features, including:
   - **Transaction Features**: Financial volume, frequency, and channel metrics.
   - **Temporal Features**: Date, time, and cyclical time-series patterns.
   - **Geographic Features**: Spatial proximity and density metrics computed via **Uber H3** and **PostGIS**.
   - **Graph Features**: Structural topology and entity relationship metrics derived via **Neo4j** and **PyTorch Geometric**.
3. **Model Training & Scoring**: Features are fed into a **LightGBM** model for training, validation, and hyperparameter tuning to generate a continuous risk or probability score for candidate locations.
4. **Ranking & Visualization**: Calculates risk probability scores for candidate withdrawal locations, ranks them in order of risk priority, and feeds the output into **Mapbox** and **Deck.gl** for hexagonal heatmap visualization.

---

# 🌍 Geospatial Data Flow

Geospatial data flows through a dual-storage and spatial-indexing approach:

- **Raw Spatial Storage**: Incoming raw GPS coordinates (latitude and longitude) are ingested into **PostGIS** to maintain precise spatial geometries.
- **Hexagonal Spatial Indexing**: Coordinates are concurrently indexed into **Uber H3** hexagonal cells.
- **Data Integration & Mapping**: Within the **PostgreSQL + H3 Extension** environment, spatial information is joined directly with ML risk predictions using unique H3 Cell IDs.
- **Visualization Output**: High-risk H3 cells are passed directly to **Mapbox** and **Deck.gl** to render dynamic risk heatmaps for operators.

---

# 🕸️ Graph Intelligence Workflow

Graph processing links complex cybercrime relationships to enhance machine learning models:

1. **Entity Extraction**: Incoming transactions and complaints are decomposed into graph entities, forming explicit relationships among victims, bank accounts, transactions, and withdrawal locations (such as ATMs).
2. **Graph Storage & Querying**: Entities and their relational edges are loaded into **Neo4j**, where relationship queries extract structural subgraphs and network features.
3. **Graph Machine Learning**: When advanced topological analysis is required, **PyTorch Geometric** processes the graph structure to generate deep graph embeddings.
4. **Feature Integration**: These graph-derived topological metrics are merged directly into the primary ML tabular feature set.

---

# ⚡ Real-Time Alert Workflow

Real-time processing ensures low-latency alert distribution upon event receipt:

1. **Event Trigger**: A new cybercrime complaint or transaction event is posted to the platform.
2. **API Gateway & Queuing**: The event enters through a **FastAPI** gateway and is queued in **Redis**.
3. **Asynchronous Execution**: **Celery** workers pull events from Redis to perform real-time model inference and risk scoring asynchronously.
4. **Notification Delivery**: If the predicted risk exceeds pre-configured operational thresholds, alerts are instantly routed through the **Twilio API** (for SMS/calls) and **Firebase Cloud Messaging (FCM)** (for mobile push notifications).

---

# 🗺️ LEA Command Dashboard

The dashboard operationalizes machine learning outputs for Law Enforcement Agencies (LEAs):

- **Backend Integration**: **FastAPI** serves model predictions, spatial overlays, and historical incident logs.
- **User Interface**: Built using **React.js** and styled with **Tailwind CSS**, providing a fast operational UI.
- **Geospatial Rendering**: Utilizes **Mapbox GL JS** and **Deck.gl** to overlay risk categories directly on an interactive map:
  - 🔴 **High Risk**: Immediate attention required.
  - 🟠 **Medium Risk**: Heightened surveillance advised.
  - 🟡 **Low Risk**: Standard monitoring.
- **Data Views**: Features interactive panels for reviewing real-time alert logs, location-specific risk scores, and historical spatial patterns.

---

# 🛠️ Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Data Engineering** | Apache Kafka, PySpark, Apache Airflow, PostgreSQL |
| **Graph Intelligence** | Neo4j, PyTorch Geometric |
| **Geospatial Intelligence** | Uber H3, PostGIS |
| **Predictive AI / ML** | Python, LightGBM, Pandas, NumPy, Scikit-learn |
| **Backend & Real-Time** | FastAPI, Redis, Celery, Twilio API, Firebase Cloud Messaging (FCM) |
| **Frontend & Visualization** | React.js, React Native, Progressive Web App (PWA), Mapbox GL JS, Deck.gl, Tailwind CSS |

---

# 🔄 End-to-End Workflow

The overall end-to-end processing pipeline operates sequentially as follows:

1. **Ingestion & Processing**: Incoming cybercrime complaints, transaction streams, GPS coordinates, and financial logs are ingested in real-time via **Apache Kafka** and processed in batch/stream using **PySpark** orchestrated by **Apache Airflow**.
2. **Storage & Spatial Indexing**: Processed data is stored in **PostgreSQL**, leveraging **PostGIS** for geometry and mapping coordinates to **Uber H3** hexagonal cell IDs.
3. **Graph & Spatial Enrichment**: Data flows into **Neo4j** for relationship analysis and **H3** for spatial analysis, combining outputs into a feature engineering matrix.
4. **Predictive Analytics**: The **LightGBM** machine learning engine scores risk levels and ranks the top-K probable locations.
5. **Serving & Alert Routing**: **FastAPI** serves predictions through **Redis** and **Celery**, triggering field updates on the **LEA Command Dashboard** (via Mapbox/Deck.gl) and push alerts via mobile notifications (**FCM** / **Twilio**).

---

# 📊 ML Evaluation

Evaluate the predictive model using metrics suited for location ranking and classification:

- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix & ROC-AUC
- **Top-K Accuracy** (primary spatial ranking metric)
- **Spatial Distance Error** (kilometers from targeted location)

### Top-K Location Prediction

The model outputs ranked candidate locations rather than a single point to maximize field utility:

```text
Predictions:
1. H3 Cell / ATM A → 0.82 → HIGH
2. H3 Cell / ATM B → 0.67 → HIGH
3. H3 Cell / ATM C → 0.41 → MEDIUM
4. H3 Cell / ATM D → 0.19 → LOW
5. H3 Cell / ATM E → 0.08 → LOW
```

---

# 🔐 Security & Privacy

- Implement **Role-Based Access Control (RBAC)** across APIs and dashboards.
- Enforce **encryption in transit (TLS)** and **at rest (AES-256)**.
- Minimize exposure of **Personally Identifiable Information (PII)** via tokenization/masking.
- Maintain comprehensive **audit logs** for analytical actions and data exports.

---

# 🚀 Future Scope

- **Graph Neural Networks (GNNs)** for dynamic entity-link prediction.
- **Temporal Modeling** using Transformer/LSTM architectures for sequential fraud paths.
- **Online Learning** to adapt continuously to emerging fraud patterns.
- **Explainable AI (XAI)** to output feature attributions alongside risk scores.

---

# 🎯 Project Goal

```text
DATA → UNDERSTANDING → PREDICTION → RISK SCORING → LOCATION RANKING → REAL-TIME ALERT → INTERVENTION
```

> **SIH26184 — Predictive analytics for proactive cybercrime intervention.**
