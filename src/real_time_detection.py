from scapy.all import sniff
from .feature_extraction import extract_features

def process_packet(packet, model, scaler):
    features = extract_features(packet)
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)
    
    if prediction[0] == 1:
        print(f"Potential intrusion detected: {packet.summary()}")

def start_detection(model, scaler, interface='eth0', count=None):
    sniff(prn=lambda pkt: process_packet(pkt, model, scaler), iface=interface, count=count)
