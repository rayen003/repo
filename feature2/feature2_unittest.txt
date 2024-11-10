import numpy as np
import unittest
from feature2 import prepare_data, SVM_model

class TestCancerClassificationModel(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.X = np.array([[1.2, 0.7], [1.6, 0.9], [1.1, 0.8], [1.5, 1.0], [0.5, 1.2], [0.3, 1.4]])
        self.y = np.array([0, 1, 0, 1, 0, 1])
        self.test_sample_size = 0.3
        self.rand_state = 42

    def test_prepare_data(self):
        # Test data preparation
        X_train, X_test, y_train, y_test = prepare_data(self.X, self.y, self.test_sample_size, self.rand_state)

        # Check sizes of splits
        self.assertEqual(len(X_train), 4)
        self.assertEqual(len(X_test), 2)

    def test_SVM_model(self):
        # Test SVM model training and evaluation
        X_train, X_test, y_train, y_test = prepare_data(self.X, self.y, self.test_sample_size, self.rand_state)
        accuracy, precision, recall, f1, y_pred = SVM_model(X_train, y_train, X_test, y_test, kernel_type='linear', rand_state=self.rand_state)

        # Validate predictions and metric outputs are within expected ranges
        self.assertIsInstance(y_pred, np.ndarray)
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

if __name__ == '__main__':
    unittest.main()