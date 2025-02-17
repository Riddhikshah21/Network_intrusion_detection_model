def extract_features(packet):
    features = [
        len(packet),
        packet.time,
        int(packet.haslayer('IP')),
        int(packet.haslayer('TCP')),
        int(packet.haslayer('UDP')),
        int(packet.haslayer('ICMP'))
    ]
    return features
