import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from scipy.io import arff

def load_and_preprocess_data(train_path, test_path):
    # Load ARFF files
    train_data, train_meta = arff.loadarff(train_path)
    test_data, test_meta = arff.loadarff(test_path)

    # Convert to pandas DataFrames
    train_df = pd.DataFrame(train_data)
    test_df = pd.DataFrame(test_data)

    # Combine train and test data for preprocessing
    data = pd.concat([train_df, test_df], axis=0)

    # Convert byte strings to regular strings (ARFF files often store strings as byte strings)
    object_columns = data.select_dtypes(include=['object']).columns
    for col in object_columns:
        data[col] = data[col].str.decode('utf-8')

    # Separate features and target
    X = data.drop('class', axis=1)
    y = data['class']

    # Identify categorical and numerical columns
    categorical_columns = X.select_dtypes(include=['object']).columns
    numerical_columns = X.select_dtypes(include=['float64', 'int64']).columns

    # Create preprocessing steps
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    numerical_transformer = StandardScaler()

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_columns),
            ('cat', categorical_transformer, categorical_columns)
        ])

    # Create preprocessing pipeline
    preprocessing_pipeline = Pipeline([
        ('preprocessor', preprocessor)
    ])

    # Fit and transform the data
    X_preprocessed = preprocessing_pipeline.fit_transform(X)

    # Convert target to binary (normal vs. anomaly)
    y_binary = np.where(y == 'normal', 0, 1)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y_binary, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, preprocessing_pipeline