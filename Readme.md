# Predictive Analytics Framework for Cybercrime Prevention[cite: 2, 3]

## 🚨 SIH26184[cite: 2, 3]

A predictive analytics platform for **forecasting likely cash-withdrawal locations from cybercrime complaints and transaction patterns**[cite: 2, 3]. The system combines large-scale data engineering, graph analytics, geospatial intelligence, machine learning, real-time alerting, and an operational dashboard[cite: 2, 3].

---

## 📌 Problem Overview[cite: 2, 3]

Cybercrime complaints contain critical data on fraudulent transactions, victims, routes, timing, and financial behavior[cite: 2, 3].

This project transforms that data into **actionable intelligence** by:[cite: 2, 3]

- Processing cybercrime and transaction data at scale[cite: 2, 3]
- Detecting entity and transaction relationships[cite: 2, 3]
- Performing geospatial analysis[cite: 2, 3]
- Predicting high-risk withdrawal locations[cite: 2, 3]
- Generating real-time alerts[cite: 2, 3]
- Displaying predictions on a command dashboard[cite: 2, 3]
- Delivering alerts to relevant stakeholders[cite: 2, 3]

---

# 🏗️ System Architecture[cite: 2, 3]

The system architecture is structured across seven core layers designed for end-to-end processing:[cite: 2, 3]

1. **Data Ingestion & ETL Layer**: Uses **Apache Kafka** for streaming incoming events, **PySpark** for distributed processing, **Apache Airflow** for workflow orchestration, and **PostgreSQL** for relational storage[cite: 2, 3].
2. **Graph Database Layer**: Employs **Neo4j** for structured graph storage and relationship querying, paired with **PyTorch Geometric** for deep learning on graph topologies[cite: 2, 3].
3. **Geospatial Indexing Layer**: Combines **PostGIS** for storing spatial geometries with **Uber H3** for hierarchical hexagonal indexing[cite: 2, 3].
4. **Predictive AI / ML Core**: Leverages **LightGBM**, **Pandas**, **NumPy**, and **Scikit-learn** in **Python** to handle feature engineering, model training, risk prediction, and ranking[cite: 2, 3].
5. **Real-Time Alert Engine**: Powered by **FastAPI** as the gateway, **Redis** for caching/queuing, **Celery** for asynchronous job execution, and APIs like **Twilio** and **Firebase Cloud Messaging (FCM)** for delivery[cite: 2, 3].
6. **LEA Command Dashboard**: A web interface built with **React.js**, **Tailwind CSS**, **Mapbox GL JS**, and **Deck.gl** to visualize risk scores, real-time alerts, and historical data[cite: 2, 3].
7. **Mobile Alerting Layer**: A mobile application built with **React Native**, **PWA**, and **Firebase Cloud Messaging (FCM)** to deliver push alerts directly to personnel in the field[cite: 2, 3].

---

# 🤖 Machine Learning Workflow[cite: 2, 3]

The ML pipeline converts historical cybercrime and transaction data into **ranked predictions of likely withdrawal locations**:[cite: 2, 3]

1. **Data Preprocessing**: Ingests raw historical transactions and cybercrime complaints, performing cleaning and normalization using **Pandas** and **NumPy**[cite: 2, 3].
2. **Feature Engineering**: Generates multi-dimensional features, including:[cite: 2, 3]
   - **Transaction Features**: Financial volume, frequency, and channel metrics[cite: 2, 3].
   - **Temporal Features**: Date, time, and cyclical time-series patterns[cite: 2, 3].
   - **Geographic Features**: Spatial proximity and density metrics computed via **Uber H3** and **PostGIS**[cite: 2, 3].
   - **Graph Features**: Structural topology and entity relationship metrics derived via **Neo4j** and **PyTorch Geometric**[cite: 2, 3].
3. **Model Training & Scoring**: Features are fed into a **LightGBM** model for training, validation, and hyperparameter tuning to generate a continuous risk or probability score for candidate locations[cite: 2, 3].
4. **Ranking & Visualization**: Calculates risk probability scores for candidate withdrawal locations, ranks them in order of risk priority, and feeds the output into **Mapbox** and **Deck.gl** for hexagonal heatmap visualization[cite: 2, 3].

---

# 🌍 Geospatial Data Flow[cite: 2, 3]

Geospatial data flows through a dual-storage and spatial-indexing approach:[cite: 2, 3]

- **Raw Spatial Storage**: Incoming raw GPS coordinates (latitude and longitude) are ingested into **PostGIS** to maintain precise spatial geometries[cite: 2, 3].
- **Hexagonal Spatial Indexing**: Coordinates are concurrently indexed into **Uber H3** hexagonal cells[cite: 2, 3].
- **Data Integration & Mapping**: Within the **PostgreSQL + H3 Extension** environment, spatial information is joined directly with ML risk predictions using unique H3 Cell IDs[cite: 2, 3].
- **Visualization Output**: High-risk H3 cells are passed directly to **Mapbox** and **Deck.gl** to render dynamic risk heatmaps for operators[cite: 2, 3].

---

# 🕸️ Graph Intelligence Workflow[cite: 2, 3]

Graph processing links complex cybercrime relationships to enhance machine learning models:[cite: 2, 3]

1. **Entity Extraction**: Incoming transactions and complaints are decomposed into graph entities, forming explicit relationships among victims, bank accounts, transactions, and withdrawal locations (such as ATMs)[cite: 2, 3].
2. **Graph Storage & Querying**: Entities and their relational edges are loaded into **Neo4j**, where relationship queries extract structural subgraphs and network features[cite: 2, 3].
3. **Graph Machine Learning**: When advanced topological analysis is required, **PyTorch Geometric** processes the graph structure to generate deep graph embeddings[cite: 2, 3].
4. **Feature Integration**: These graph-derived topological metrics are merged directly into the primary ML tabular feature set[cite: 2, 3].

---

# ⚡ Real-Time Alert Workflow[cite: 2, 3]

Real-time processing ensures low-latency alert distribution upon event receipt:[cite: 2, 3]

1. **Event Trigger**: A new cybercrime complaint or transaction event is posted to the platform[cite: 2, 3].
2. **API Gateway & Queuing**: The event enters through a **FastAPI** gateway and is queued in **Redis**[cite: 2, 3].
3. **Asynchronous Execution**: **Celery** workers pull events from Redis to perform real-time model inference and risk scoring asynchronously[cite: 2, 3].
4. **Notification Delivery**: If the predicted risk exceeds pre-configured operational thresholds, alerts are instantly routed through the **Twilio API** (for SMS/calls) and **Firebase Cloud Messaging (FCM)** (for mobile push notifications)[cite: 2, 3].

---

# 🗺️ LEA Command Dashboard[cite: 2, 3]

The dashboard operationalizes machine learning outputs for Law Enforcement Agencies (LEAs):[cite: 2, 3]

- **Backend Integration**: **FastAPI** serves model predictions, spatial overlays, and historical incident logs[cite: 2, 3].
- **User Interface**: Built using **React.js** and styled with **Tailwind CSS**, providing a fast operational UI[cite: 2, 3].
- **Geospatial Rendering**: Utilizes **Mapbox GL JS** and **Deck.gl** to overlay risk categories directly on an interactive map:[cite: 2, 3]
  - 🔴 **High Risk**: Immediate attention required[cite: 2, 3].
  - 🟠 **Medium Risk**: Heightened surveillance advised[cite: 2, 3].
  - 🟡 **Low Risk**: Standard monitoring[cite: 2, 3].
- **Data Views**: Features interactive panels for reviewing real-time alert logs, location-specific risk scores, and historical spatial patterns[cite: 2, 3].

---

# 🛠️ Technology Stack[cite: 2, 3]

| Category | Technologies |
| :--- | :--- |
| **Data Engineering** | Apache Kafka, PySpark, Apache Airflow, PostgreSQL |[cite: 3]
| **Graph Intelligence** | Neo4j, PyTorch Geometric |[cite: 3]
| **Geospatial Intelligence** | Uber H3, PostGIS |[cite: 3]
| **Predictive AI / ML** | Python, LightGBM, Pandas, NumPy, Scikit-learn |[cite: 3]
| **Backend & Real-Time** | FastAPI, Redis, Celery, Twilio API, Firebase Cloud Messaging (FCM) |[cite: 3]
| **Frontend & Visualization** | React.js, React Native, Progressive Web App (PWA), Mapbox GL JS, Deck.gl, Tailwind CSS |[cite: 3]

---

# 🔄 End-to-End Workflow[cite: 2, 3]

The overall end-to-end processing pipeline operates sequentially as follows:[cite: 2, 3]

1. **Ingestion & Processing**: Incoming cybercrime complaints, transaction streams, GPS coordinates, and financial logs are ingested in real-time via **Apache Kafka** and processed in batch/stream using **PySpark** orchestrated by **Apache Airflow**[cite: 2, 3].
2. **Storage & Spatial Indexing**: Processed data is stored in **PostgreSQL**, leveraging **PostGIS** for geometry and mapping coordinates to **Uber H3** hexagonal cell IDs[cite: 2, 3].
3. **Graph & Spatial Enrichment**: Data flows into **Neo4j** for relationship analysis and **H3** for spatial analysis, combining outputs into a feature engineering matrix[cite: 2, 3].
4. **Predictive Analytics**: The **LightGBM** machine learning engine scores risk levels and ranks the top-K probable locations[cite: 2, 3].
5. **Serving & Alert Routing**: **FastAPI** serves predictions through **Redis** and **Celery**, triggering field updates on the **LEA Command Dashboard** (via Mapbox/Deck.gl) and push alerts via mobile notifications (**FCM** / **Twilio**)[cite: 2, 3].

---

# 📊 ML Evaluation[cite: 2, 3]

Evaluate the predictive model using metrics suited for location ranking and classification:[cite: 2, 3]

- Accuracy, Precision, Recall, F1-Score[cite: 3]
- Confusion Matrix & ROC-AUC[cite: 3]
- **Top-K Accuracy** (primary spatial ranking metric)[cite: 3]
- **Spatial Distance Error** (kilometers from targeted location)[cite: 3]

### Top-K Location Prediction[cite: 2, 3]

The model outputs ranked candidate locations rather than a single point to maximize field utility:[cite: 2, 3]

```text
Predictions:
1. H3 Cell / ATM A → 0.82 → HIGH
2. H3 Cell / ATM B → 0.67 → HIGH
3. H3 Cell / ATM C → 0.41 → MEDIUM
4. H3 Cell / ATM D → 0.19 → LOW
5. H3 Cell / ATM E → 0.08 → LOW
```[cite: 2, 3]

---

# 🔐 Security & Privacy[cite: 2, 3]

- Implement **Role-Based Access Control (RBAC)** across APIs and dashboards[cite: 3].
- Enforce **encryption in transit (TLS)** and **at rest (AES-256)**[cite: 3].
- Minimize exposure of **Personally Identifiable Information (PII)** via tokenization/masking[cite: 3].
- Maintain comprehensive **audit logs** for analytical actions and data exports[cite: 3].

---

# 🚀 Future Scope[cite: 2, 3]

- **Graph Neural Networks (GNNs)** for dynamic entity-link prediction[cite: 3].
- **Temporal Modeling** using Transformer/LSTM architectures for sequential fraud paths[cite: 3].
- **Online Learning** to adapt continuously to emerging fraud patterns[cite: 3].
- **Explainable AI (XAI)** to output feature attributions alongside risk scores[cite: 3].

---

# 🎯 Project Goal[cite: 3]

```text
DATA → UNDERSTANDING → PREDICTION → RISK SCORING → LOCATION RANKING → REAL-TIME ALERT → INTERVENTION
```[cite: 3]

> **SIH26184 — Predictive analytics for proactive cybercrime intervention.**[cite: 2, 3]