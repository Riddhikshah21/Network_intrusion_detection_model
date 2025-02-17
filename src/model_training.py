from sklearn.metrics import classification_report, confusion_matrix
from models.random_forest import create_rf_model

def train_and_evaluate_model(X_train, y_train, X_test, y_test, n_estimators=100, random_state=42):
    model = create_rf_model(n_estimators, random_state)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    report = classification_report(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    return model, {'classification_report': report, 'confusion_matrix': conf_matrix}
