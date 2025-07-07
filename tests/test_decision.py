import unittest
from decision_engine.decision import make_scaling_decision

class TestScalingDecision(unittest.TestCase):
    def test_scale_up(self):
        self.assertEqual(make_scaling_decision(85), "scale_up")

    def test_scale_down(self):
        self.assertEqual(make_scaling_decision(15), "scale_down")

    def test_no_action(self):
        self.assertEqual(make_scaling_decision(50), "no_action")

if __name__ == '__main__':
    unittest.main()

