import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import zscore
import matplotlib.pyplot as plt
import os

def is_anomaly(current_cpu, cpu_history, threshold=2.0):
    """
    Detect if current CPU usage is an anomaly using z-score.
    """
    if len(cpu_history) < 5:
        return False  # Not enough data for reliable detection

    z_scores = zscore(cpu_history)
    latest_z = z_scores[-1]
    return abs(latest_z) > threshold

def forecast_demand(df=None, threshold=2.0):
    """
    Predict future CPU usage using linear regression and check for anomalies.
    Accepts optional DataFrame input for testing.
    """
    if df is None:
        filepath = 'data/metrics.csv'
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Missing metrics file: {filepath}")
        df = pd.read_csv(filepath, names=['timestamp', 'cpu_usage', 'memory_usage'], skiprows=1)

    df['index'] = range(len(df))

    # Train linear regression model
    X = df[['index']]
    y = df['cpu_usage']
    model = LinearRegression()
    model.fit(X, y)

    # Predict next value
    future_index = np.array([[len(df) + 1]])
    predicted_cpu = model.predict(future_index)[0]

    # Detect anomaly
    current_cpu = y.values[-1]
    anomaly = is_anomaly(current_cpu, y.values, threshold=threshold)

    # Log anomaly if needed
    if anomaly:
        os.makedirs('logs', exist_ok=True)
        with open('logs/anomalies.log', 'a') as log_file:
            log_file.write(f"[{df['timestamp'].iloc[-1]}] Anomaly detected: CPU = {current_cpu:.2f}%\n")

    return predicted_cpu, anomaly

def plot_cpu_trend():
    """
    Plot historical CPU usage from metrics.csv and show it briefly.
    """
    filepath = 'data/metrics.csv'
    if not os.path.exists(filepath):
        print("No metrics file found to plot.")
        return

    df = pd.read_csv(filepath, names=['timestamp', 'cpu_usage', 'memory_usage'], skiprows=1)

    if df.empty:
        print("Metrics file is empty. Cannot plot.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['cpu_usage'], marker='o', linestyle='-', color='blue', label='CPU Usage (%)')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Timestamp')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage Over Time')
    plt.tight_layout()
    plt.legend()
    plt.grid(True)

    # Show the graph for 3 seconds then close
    plt.show(block=False)
    plt.pause(3)
    plt.close()
