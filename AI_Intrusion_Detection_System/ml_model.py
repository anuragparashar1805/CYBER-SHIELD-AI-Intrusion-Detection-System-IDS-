import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle


# 1. Dummy dataset creation for demonstration training
def train_mock_model():
    # Features: [packet_length, protocol_numeric, flags/ports]
    # Protocols: 6=TCP, 17=UDP, 1=ICMP
    X = np.array([
        [64, 6, 80], [1500, 6, 443], [60, 17, 53],  # Normal Traffic
        [1000, 6, 80], [1000, 6, 80], [1000, 6, 80],  # Potential DDoS (Repeated big packets)
        [40, 6, 21], [40, 6, 22], [40, 6, 23]  # Port Scan (Tiny packets hitting multiple ports)
    ])

    # Labels: 0 = Normal, 1 = DDoS, 2 = Port Scan
    y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])

    model = RandomForestClassifier(n_estimators=10)
    model.fit(X, y)

    # Save model to disk
    with open('ids_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("AI Model Trained and Saved.")


def predict_packet(length, protocol, port):
    try:
        with open('ids_model.pkl', 'rb') as f:
            model = pickle.load(f)
    except FileNotFoundError:
        train_mock_model()
        with open('ids_model.pkl', 'rb') as f:
            model = pickle.load(f)

    prediction = model.predict([[length, protocol, port]])[0]
    mapping = {0: "Normal", 1: "DDoS Attack", 2: "Port Scan"}
    return mapping.get(prediction, "Unknown")


if __name__ == "__main__":
    train_mock_model()