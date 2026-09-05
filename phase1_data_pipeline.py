import h3
import numpy as np
import pandas as pd
from faker import Faker

# Initialize random seed and generator
np.random.seed(42)
fake = Faker()

# Step 1: Generate Mock ATM/Terminal Database
def generate_atm_terminals(num_terminals=50):
    # Centered around urban center coordinates (e.g., Delhi NCR region)
    base_lat, base_lng = 28.6139, 77.2090
    terminals = []

    for i in range(num_terminals):
        lat = base_lat + np.random.uniform(-0.05, 0.05)
        lng = base_lng + np.random.uniform(-0.05, 0.05)
        # H3 Spatial Indexing (Resolution 8 ~0.73 sq km per cell)
        h3_index = h3.latlng_to_cell(lat, lng, 8)

        terminals.append(
            {
                "terminal_id": f"ATM_{i+1000}",
                "latitude": lat,
                "longitude": lng,
                "h3_cell_id": h3_index,
                "terminal_type": np.random.choice(["ATM", "POS", "MICRO_ATM"]),
            }
        )

    return pd.DataFrame(terminals)


# Step 2: Generate Mock Transactions & Cybercrime Complaint Logs
def generate_transaction_logs(df_terminals, num_records=1000):
    logs = []
    terminal_ids = df_terminals["terminal_id"].tolist()

    for _ in range(num_records):
        terminal = df_terminals.sample(1).iloc[0]
        # Simulate fraud flag: 15% rate for high-volume cash-out simulation
        is_fraud = 1 if np.random.rand() < 0.15 else 0

        logs.append(
            {
                "transaction_id": fake.uuid4(),
                "complaint_id": f"NCRP_{fake.random_number(digits=6)}",
                "source_account": f"ACC_{fake.random_number(digits=5)}",
                "target_account": f"MULE_{fake.random_number(digits=5)}",
                "amount": np.random.randint(1000, 100000),
                "timestamp": fake.date_time_this_month(),
                "terminal_id": terminal["terminal_id"],
                "h3_cell_id": terminal["h3_cell_id"],
                "terminal_type": terminal["terminal_type"],
                "is_fraud_cashout": is_fraud,  # Target variable
            }
        )

    df_logs = pd.DataFrame(logs)
    df_logs["timestamp"] = pd.to_datetime(df_logs["timestamp"])
    return df_logs


if __name__ == "__main__":
    # Execute Phase 1 Pipeline
    df_terminals = generate_atm_terminals(num_terminals=100)
    df_logs = generate_transaction_logs(df_terminals, num_records=2000)

    # Save to local CSV files (simulating database tables)
    df_terminals.to_csv("atm_terminals.csv", index=False)
    df_logs.to_csv("transaction_logs.csv", index=False)

    print("Phase 1 Complete: Generated synthetic logs and indexed spatial data.")