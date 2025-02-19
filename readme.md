**Network Intrusion Detection System Using Machine Learning**

This project implements a Network Intrusion Detection System (NIDS) leveraging machine learning algorithms to identify and prevent unauthorized activities within a network. By analyzing network traffic data, the system distinguishes between normal and malicious behavior, enhancing cybersecurity defenses.

*Installation*

1. Clone the Repository:
git clone https://github.com/Riddhikshah21/Network_intrusion_detection_model.git

2. Create a Virtual Environment:
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies:
pip install -r requirements.txt

Dataset used: The system has been tested with the following dataset
NSL-KDD: An improved version of the KDD'99 dataset, addressing redundancy and imbalance issues.

The following machine learning algorithm have been implemented and evaluated:
Random Forest Classifier: An ensemble method that builds multiple decision trees and merges their results for more accurate and stable predictions.

After training and evaluating the models, the following results were obtained:
Accuracy: Percentage of correctly classified instances.
Precision: Proportion of true positive results among all positive predictions.
Recall: Proportion of true positive results among all actual positives.
F1-Score: Harmonic mean of precision and recall.