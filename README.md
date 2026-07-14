# ⚡ CYBER-SHIELD AI // Intrusion Detection System (IDS)

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blueviolet?style=flat-square&logo=python)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-00ffcc?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![ML Core](https://img.shields.io/badge/ML%20Engine-Scikit--Learn-ff0055?style=flat-square&logo=scikit-learn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

An advanced, real-time AI-Powered Intrusion Detection System featuring a high-throughput network packet sniffing loop, multi-class machine learning threat classification, and an asynchronous, futuristic cyberpunk command dashboard. 

Instead of traditional enterprise tools relying on fragile signature catalogs, **CYBER-SHIELD AI** isolates malicious activity by parsing structural data anomalies across network streams in real time.

---

## ⚡ Core Architecture & Key Features

*   📊 **Live Analytical Dashboard:** A high-contrast, dark-theme cockpit dashboard that updates metrics, threat vectors, and data visualizations dynamically using **Chart.js**.
*   🏎️ **Sub-Millisecond Processing Loop:** Implements multi-threaded background packet capturing utilizing **Scapy** to ensure zero packet drop rates during dense local traffic spikes.
*   🧠 **AI Threat Multi-Classification:** Replaces basic binary security states with an optimized **Random Forest Ensemble** capable of diagnosing specific threat signatures (e.g., Volumetric DDoS, Low-and-Slow Port Scans).
*   🗃️ **Log Management & Persistence:** Thread-safe ACID-compliant persistence using an embedded **SQLite** layer for instant query execution and incident analysis.
*   📬 **Automated Severity Alerts:** System monitors threat vectors and flags anomalies categorized by high/medium severity indices for rapid administrative incident response.

---

## 🛠️ The Strategic Technology Stack

| Layer | Component Technology | Role in Architecture |
| :--- | :--- | :--- |
| **Backend Core** | `Python 3.x Engine` | Foundation for multi-threaded background task orchestration. |
| **Ingestion Engine**| `Scapy Framework` | Bypasses standard OS network layers to pull raw socket data. |
| **Predictive Layer**| `Scikit-Learn Ensemble` | Runs high-speed Random Forest decision matrices. |
| **Data Formatting**| `Pandas & NumPy` | Structures messy packet frames into dimensional vectors. |
| **Storage Layer** | `SQLite Embedded Engine` | Low-overhead relational storage for threat logging. |
| **Web Gateway** | `Flask Framework` | Hosts internal API infrastructure to serve real-time clients. |
| **Cockpit GUI** | `HTML5 / Neon CSS3 / JS` | High-fidelity, cyberpunk web control terminal interface. |

---

## 📁 Repository Blueprint

```text
AI_Intrusion_Detection_System/
│
├── app.py                 # Main Flask server gateway & API router
├── packet_sniffer.py      # Multi-threaded Scapy packet processing core
├── ml_model.py            # Random Forest training & classification logic
├── database.py            # SQLite table initialization and logging helpers
├── ids_log.db             # Embedded relational database (auto-generated)
├── requirements.txt       # Unified project dependency manifesto
│
├── static/                # Asynchronous frontend dashboard assets
│   ├── css/
│   │   └── style.css      # Futuristic styling layout (cyberpunk neon theme)
│   └── js/
│       └── dashboard.js   # Live API polling loop & Chart.js renderer
│
└── templates/
    └── dashboard.html     # Structural cockpit layout document
