import unittest
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from feature1 import drop_nan_columns, split_features_and_labels, perform_PCA

class TestCancerDetectionFeatures(unittest.TestCase):

    def setUp(self):
        # Setup a sample DataFrame for testing
        self.df = pd.DataFrame({
            'feature1': [1.0, 2.0, np.nan, 4.0],
            'feature2': [np.nan, 2.0, 3.0, 4.0],
            'feature3': ['A', 'B', 'A', 'B'],
            'diagnosis': ['M', 'B', 'M', 'B']
        })

    def test_drop_nan_columns(self):
        df_cleaned = drop_nan_columns(self.df)
        # Check that columns with NaN values are dropped
        self.assertNotIn('feature1', df_cleaned.columns)
        self.assertNotIn('feature2', df_cleaned.columns)

    def test_split_features_and_labels(self):
        features, labels = split_features_and_labels(self.df, 'diagnosis')
        # Check that the features DataFrame does not contain the label column
        self.assertNotIn('diagnosis', features.columns)

    def test_perform_PCA(self):
        scaler = StandardScaler()
        df_features = self.df[['feature1', 'feature2']].dropna()
        df_features_scaled = scaler.fit_transform(df_features)
        pca_result = perform_PCA(df_features_scaled, 2, scaler=scaler)
        # Check that the PCA result has the expected number of components
        self.assertEqual(pca_result.shape[1], 2)

if __name__ == '__main__':
    unittest.main()
