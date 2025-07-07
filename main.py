from monitoring.monitor import collect_metrics
from prediction.predictor import forecast_demand, plot_cpu_trend
from decision_engine.decision import make_scaling_decision
from scaling.scaler import execute_scaling

def main():
    # Step 1: Collect metrics
    metrics = collect_metrics()

    # Step 2: Forecast demand and check for anomaly
    predicted_cpu, anomaly = forecast_demand(metrics)

    # Step 3: Decide what to do
    decision = make_scaling_decision(predicted_cpu)

    # Step 4: React to anomaly (optional alert)
    if anomaly:
        print("⚠️ Anomaly detected in CPU usage!")

    # Step 5: Execute scaling
    execute_scaling(decision)

    # Step 6: Show CPU trend plot
    plot_cpu_trend()

if __name__ == "__main__":
    main()
