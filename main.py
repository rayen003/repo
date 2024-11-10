import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from feature1.feature1 import *
from feature2.feature2 import *
from feature3.feature3 import *



if __name__ == "__main__":
    # Load the data
    data = pd.read_csv('Cancer_Data.csv')

    # Clean data (drop columns with NaN values)
    data_cleaned = drop_nan_columns(data)

    # Split data into features and labels
    label_column = 'diagnosis'
    features, labels = split_features_and_labels(data_cleaned, label_column)

    # Perform PCA (dimensionality reduction)
    scaler = StandardScaler()
    pca_components = 5
    data_PCA = perform_PCA(features, pca_components, scaler)

    # Prepare data for training and testing
    test_size = 0.2
    random_state = 42
    X_train, X_test, y_train, y_test = prepare_data(data_PCA, labels, test_size, random_state)

    # Train SVM model and evaluate
    kernel_type = 'linear'
    accuracy, precision, recall, f1, y_pred = SVM_model(X_train, y_train, X_test, y_test, kernel_type, random_state)

  

 