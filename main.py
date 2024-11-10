import pandas as pd
from feature1.feature1 import drop_nan_columns, split_features_and_labels, perform_PCA
from feature2.feature2 import prepare_data, SVM_model
from feature3.feature3 import load_data, separate_data_by_diagnosis, calculate_statistics, plot_data
from sklearn.preprocessing import StandardScaler

if __name__ == "__main__":
    # Load the data
    data = load_data('Cancer_Data.csv')  
    
    # Clean the data
    data_cleaned = drop_nan_columns(data)
    
    # Separate the data by diagnosis
    malignant, benign = separate_data_by_diagnosis(data_cleaned)
    
    # Calculate statistics for specific features
    features = ['radius_mean', 'texture_mean']  
    analysis = calculate_statistics(malignant, benign, features)
    
    for feature, stats in analysis.items():
        print(f"Feature: {feature}")
        for diagnosis, values in stats.items():
            print(f"  {diagnosis}:")
            for stat_name, value in values.items():
                print(f"    {stat_name}: {value}")
    
    # Prepare data for SVM model
    X, y = split_features_and_labels(data_cleaned, 'diagnosis')  
    test_sample_size = 0.2  # 20% for testing
    rand_state = 42  # Random state for reproducibility
    X_train, X_test, y_train, y_test = prepare_data(X, y, test_sample_size, rand_state)
    
    # Perform PCA
    n_of_components = 2  
    scaler = StandardScaler()  
    X_train_pca = perform_PCA(X_train, n_of_components, scaler)
    X_test_pca = perform_PCA(X_test, n_of_components, scaler)
    
    # Train SVM model
    kernel_type = 'linear' 
    accuracy, precision, recall, f1, y_pred = SVM_model(X_train_pca, y_train, X_test_pca, y_test, kernel_type, rand_state)
    
    # Plot the data
    plot_data(malignant, benign)