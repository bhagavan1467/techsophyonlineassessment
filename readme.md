# 🔧 Smart Application Performance Monitoring and Auto-Scaling System

This project implements an intelligent, modular system that automatically monitors, predicts, and adjusts cloud infrastructure resources based on predicted CPU demand. It includes anomaly detection, real-time trend visualization, and optional integration with AWS EC2.

---

## 📌 Features

✅ Modular architecture:

- **Monitoring** – collects performance metrics
- **Prediction** – uses ML to forecast CPU usage
- **Anomaly Detection** – flags abnormal spikes
- **Decision Engine** – determines whether to scale up/down
- **Scaler** – executes real or simulated scaling (supports AWS)

✅ Time Series Forecasting using `LinearRegression`\
✅ Z-Score–based Anomaly Detection\
✅ Graphical visualization of CPU usage trend\
✅ Logs anomalies to `logs/anomalies.log`\
✅ Unit tests for forecasting and scaling logic\
✅ AWS EC2 scaling integration (optional, real-time)

---

## 📂 Project Structure

```
smart_auto_scaling/
│
├── monitoring/
│   └── monitor.py
├── prediction/
│   └── predictor.py
├── decision_engine/
│   └── decision.py
├── scaling/
│   └── scaler.py
│
├── data/
│   └── metrics.csv         # generated dynamically
├── logs/
│   └── anomalies.log       # generated dynamically
│
├── tests/
│   ├── test_prediction.py
│   └── test_decision.py
│
├── main.py
└── README.md
```

---

## 🚀 How It Works

1. `main.py` runs the system end-to-end
2. Simulated CPU + memory metrics are saved to `metrics.csv`
3. ML model predicts future CPU usage
4. If predicted CPU > 75% → scale up\
   If < 25% → scale down\
   Otherwise → no action
5. Anomalies in CPU are detected and logged
6. Optional AWS EC2 scaling (real or simulated)

---

## 📈 Sample Output

```bash
Collected CPU: 82.3%
Predicted CPU: 89.1%
⚠️  Anomaly detected in CPU usage!
Scaling up via AWS EC2...
```

---

## ✅ Run the System

### Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pandas numpy matplotlib scikit-learn boto3 scipy
```

### Run the program:

```bash
python main.py
```

---

## ✅ Run Tests

```bash
python -m unittest discover tests
```

---

## 🔐 AWS Integration (Optional)

To enable real EC2 scaling:

1. Install and configure AWS CLI:

```bash
aws configure
```

2. Update `scaler.py` with your instance ID
3. Uncomment boto3 logic

---

## 📊 Plotting

The system will show a CPU usage graph for 3 seconds after each run.

---

## 📒 Example Use Cases

- Smart cloud cost optimization
- Load-aware auto-scaling system
- Performance anomaly detection
- Capstone/academic project in AI + Cloud

---

## 🙌 Contributors

- **Your Name** – Developer, ML Integration, AWS Connector

---

## 📜 License

MIT License (or specify your own)

