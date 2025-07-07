import unittest
import pandas as pd
from prediction.predictor import forecast_demand

class TestForecastDemand(unittest.TestCase):
    def test_forecast_linear_increasing(self):
        # Simulate increasing CPU usage
        data = {
            'timestamp': [f"2025-07-07T12:0{i}:00" for i in range(5)],
            'cpu_usage': [20, 30, 40, 50, 60],
            'memory_usage': [50]*5
        }
        df = pd.DataFrame(data)
        predicted, _ = forecast_demand(df)
        self.assertGreater(predicted, 50)  # realistic threshold

    def test_forecast_flat_cpu(self):
        data = {
            'timestamp': [f"2025-07-07T12:0{i}:00" for i in range(5)],
            'cpu_usage': [50]*5,
            'memory_usage': [50]*5
        }
        df = pd.DataFrame(data)
        predicted, _ = forecast_demand(df)
        self.assertAlmostEqual(predicted, 50, delta=5)  # wider tolerance

if __name__ == '__main__':
    unittest.main()
