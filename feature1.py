
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
#from sklearn.preprocessing import StandardScaler
#Bug we can use
"""

Feature 1 description: 

- Prepare the feature matrix for the cancer detection model
- Data cleaning and manipulation

"""




def drop_nan_columns(df):
    """
    Drops columns containing NaN values in the provided DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame to clean.

    Returns:
        pd.DataFrame: A new DataFrame with columns containing NaN values removed.
    """
    print(df.isna().sum())
    df_cleaned = df.dropna(axis=1)
    
    return df_cleaned

def split_features_and_labels(df):
    """
    Splits the DataFrame into features and label vector for classification.

    Args:
        df (pd.DataFrame): The input DataFrame containing features and a 'diagnosis' column as the label.

    Returns:
        tuple: A tuple containing:
            - features (pd.DataFrame): DataFrame of features with the 'diagnosis' column removed.
            - y (np.ndarray): NumPy array representing the binary label vector where 'M' is mapped to 1 and 'B' to 0.
    """
    features = df.drop('diagnosis', axis=1)
    y = np.array(df.diagnosis.map({'M': 1, 'B': 0}))
    return features, y


def perform_PCA(df):
    """
    Performs PCA on the input DataFrame to reduce dimensionality to 2 components.

    Args:
        df (pd.DataFrame or np.ndarray): The input feature DataFrame or array.

    Returns:
        np.ndarray: A NumPy array with the reduced feature set, containing 2 principal components.
    """
    pca_model = PCA(n_components=2)
    data_PCA = pca_model.fit_transform(df)
    return data_PCA

#Get the data set
cancer_data = pd.read_csv('Cancer_Data.csv')


#Get our clean data
cancer_data_cleaned = drop_nan_columns(cancer_data)

#Get our label vector and feature matrix
X,y = split_features_and_labels(cancer_data_cleaned)

#Reduce our features while keeping most of the variance
X_PCA = perform_PCA(X)


