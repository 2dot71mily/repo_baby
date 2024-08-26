import unittest
import numpy as np
from logistic_regression import LogisticRegression

class TestLogisticRegression(unittest.TestCase):
    def setUp(self):
        self.model = LogisticRegression(learning_rate=0.1, num_iterations=1000)

    def test_sigmoid(self):
        self.assertAlmostEqual(self.model.sigmoid(0), 0.5)
        self.assertAlmostEqual(self.model.sigmoid(10), 0.9999, places=2)
        self.assertAlmostEqual(self.model.sigmoid(-10), 0.0001, places=2)

    def test_fit_predict(self):
        X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
        y = np.array([0, 0, 1, 1])
        
        self.model.fit(X, y)
        predictions = self.model.predict(X)
        
        self.assertEqual(len(predictions), len(y))
        self.assertTrue(all(isinstance(pred, int) for pred in predictions))
        self.assertTrue(all(pred in [0, 1] for pred in predictions))

    def test_accuracy(self):
        y_true = np.array([0, 1, 1, 0, 1])
        y_pred = np.array([0, 1, 1, 1, 1])
        
        accuracy = self.model.accuracy(y_true, y_pred)
        self.assertAlmostEqual(accuracy, 0.8)

if __name__ == '__main__':
    unittest.main()