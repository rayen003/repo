

from feature1 import X_PCA, y

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score, recall_score, f1_score


"""

Feature 2 description: 

- Perform a clasiffication model that classifies pacients as malign or benign
- We use a Support Vector Machine supervised learning model to predict that

"""


#Fixed: added test_sample_size and rand_state to let user choose their test split parameters
def prepare_data(X,y,test_sample_size,rand_state):
    """
    
    Prepare data for our model it splits both the feature matrix and label vector to train and test

    Args:
        X (np.ndarray or pd.DataFrame): feature matrix
        y (np.ndarray or pd.DataFrame): label vector
        rand_state (int): random state for split
        test_sample_size (float68): select percentage of test sample

    Returns:
        tuple: Tuple with len = 4:
        - X_train: training feature matrix
        - X_test: testing feature matrix
        - y_train: training label vector
        - y_test: testing label vector
    """
    
    X_train,X_test, y_train,y_test =train_test_split(X,y,test_size=test_sample_size,random_state=rand_state)
    return  X_train,X_test, y_train,y_test


#Added kernel and random_state as a parameter
#Added more metrics for model performance: preciion,recal,f1
def SVM_model(X_train, y_train, X_test, y_test, kernel_type, rand_state):
    """
    Trains an SVM model on the provided training data and evaluates it on the test data.

    Args:
        X_train (np.ndarray or pd.DataFrame): Training feature matrix.
        y_train (np.ndarray or pd.Series): Training label vector.
        X_test (np.ndarray or pd.DataFrame): Testing feature matrix.
        y_test (np.ndarray or pd.Series): Testing label vector.
        kernel_type (str): Kernel type for the SVM model.
        rand_state (int): Random state for the SVM model.

    Returns:
        tuple: A tuple containing:
            - accuracy (float): Accuracy of the SVM model on the test set.
            - precision (float): Precision of the SVM model on the test set.
            - recall (float): Recall of the SVM model on the test set.
            - f1 (float): F1 score of the SVM model on the test set.
            - y_pred (np.ndarray): Predicted labels for the test set.
    """
    # Initialize the SVM model with specified kernel and random state
    svm_model = SVC(kernel=kernel_type, random_state=rand_state)
    
    # Train the model
    svm_model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = svm_model.predict(X_test)
    
    # Calculate accuracy, precision, recall, and F1 score
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Print accuracy metrics
    print("SVM Model Accuracy:", accuracy)
    print("SVM Model Precision:", precision)
    print("SVM Model Recall:", recall)
    print("SVM Model F1 Score:", f1)
    
    return accuracy, precision, recall, f1, y_pred


