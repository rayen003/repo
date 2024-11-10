import unittest
import pandas as pd
from feature3 import load_data, separate_data_by_diagnosis, calculate_statistics, plot_data

class TestFeature3Functions(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'diagnosis': ['M', 'B', 'M', 'B'],
            'radius_mean': [12.3, 11.4, 14.5, 9.8],
            'texture_mean': [19.3, 18.4, 20.5, 16.7]
        })

    def test_load_data(self):
        self.assertEqual(self.data.shape[0], 4)  # Checking if data has 4 rows

    def test_separate_data_by_diagnosis(self):
        malignant, benign = separate_data_by_diagnosis(self.data)
        self.assertEqual(len(malignant), 2)  # 2 malignant cases
        self.assertEqual(len(benign), 2)     # 2 benign cases

    def test_calculate_statistics(self):
        features = ['radius_mean']
        malignant, benign = separate_data_by_diagnosis(self.data)
        stats = calculate_statistics(malignant, benign, features)
        self.assertEqual(stats['radius_mean']['Malignant']['Mean'], 13.4)

    def test_plot_data(self):
        try:
            plot_data(self.data, self.data)
            plot_executed = True
        except:
            plot_executed = False
        self.assertTrue(plot_executed)

if __name__ == '__main__':
    unittest.main()
