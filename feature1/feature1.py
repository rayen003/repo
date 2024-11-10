import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

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
    df_cleaned = df.dropna(axis=1)
    return df_cleaned

# User can choose label as a param
# Now returns a series binary mapped and a dataframe
# Added error handling
def split_features_and_labels(df, label):
    """
    Splits the DataFrame into features and a binary-mapped label series for classification.

    Args:
        df (pd.DataFrame): The input DataFrame containing features and a label column specified by `label`.
        label (str): The name of the column to be used as the label.

    Returns:
        tuple: A tuple containing:
            - features (pd.DataFrame): DataFrame of features with the specified label column removed.
            - y (pd.Series): Series representing the binary-mapped label vector, with two unique string values mapped to 0 and 1.
    """
    # Check if label column exists
    if label not in df.columns:
        raise ValueError(f"The label '{label}' does not exist in the DataFrame.")

    # Get the unique categories in the label column
    categories = df[label].unique()
    
    # Ensure there are exactly two unique categories
    if len(categories) != 2:
        raise ValueError("Label column must contain exactly two categories.")
    
    # Map the categories to 0 and 1
    y = df[label].map({categories[0]: 0, categories[1]: 1})
    
    # Drop the label column from the features
    features = df.drop(label, axis=1)
    
    return features, y

# Added variable for number of components
# Added variable for scaling our data
def perform_PCA(df, n_of_components, scaler):
    """
    Performs PCA on the input DataFrame to reduce dimensionality.

    Args:
        df (pd.DataFrame or np.ndarray): The input feature DataFrame or array.
        n_of_components (int): The number of principal components to keep.
        scaler (object): A scaler instance for standardizing the data before PCA.

    Returns:
        np.ndarray: A NumPy array with the reduced feature set.
    """
    # Check if n_of_components is valid
    if n_of_components > df.shape[1]:
        raise ValueError("`n_of_components` cannot be greater than the number of features.")
    
    df_scaled = scaler.fit_transform(df)
    pca_model = PCA(n_components=n_of_components)
    data_PCA = pca_model.fit_transform(df_scaled)
    return data_PCA

