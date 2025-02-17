from sklearn.ensemble import RandomForestClassifier

def create_rf_model(n_estimators=100, random_state=42):
    return RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
