import yaml
from src.data_preprocessing import load_and_preprocess_data
from src.model_training import train_and_evaluate_model
from src.real_time_detection import start_detection

def main():
    # Load configuration
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # Load and preprocess data
    X_train, X_test, y_train, y_test, scaler = load_and_preprocess_data(
        config['data']['train_path'], 
        config['data']['test_path']
    )

    # Train and evaluate model
    model, metrics = train_and_evaluate_model(
        X_train, y_train, X_test, y_test,
        n_estimators=config['model']['n_estimators'],
        random_state=config['model']['random_state']
    )

    print("Model Evaluation Metrics:")
    print(metrics['classification_report'])
    print("Confusion Matrix:")
    print(metrics['confusion_matrix'])


    # Start real-time detection
    # print("Starting real-time detection...")
    # start_detection(
    #     model, 
    #     scaler,
    #     interface=config['detection']['interface'],
    #     count=config['detection']['packet_count']
    # )

if __name__ == "__main__":
    main()
