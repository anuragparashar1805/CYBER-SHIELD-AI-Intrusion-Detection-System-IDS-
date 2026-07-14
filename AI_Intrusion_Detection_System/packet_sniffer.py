from scapy.all import sniff, IP, TCP, UDP
from ml_model import predict_packet
from database import log_alert
import threading

# Shared memory variable to display on the live dashboard
latest_metrics = {
    "total_packets": 0,
    "normal": 0,
    "ddos": 0,
    "port_scan": 0
}


def process_packet(packet):
    global latest_metrics
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        length = len(packet)

        # Get Destination Port safely
        port = 0
        if TCP in packet:
            port = packet[TCP].dport
        elif UDP in packet:
            port = packet[UDP].dport

        # ML Analysis
        attack_type = predict_packet(length, proto, port)

        # Metric Counting
        latest_metrics["total_packets"] += 1
        if attack_type == "Normal":
            latest_metrics["normal"] += 1
        elif attack_type == "DDoS Attack":
            latest_metrics["ddos"] += 1
            log_alert(src_ip, dst_ip, str(proto), length, attack_type, "High")
            # trigger_email_alert() could be called here
        elif attack_type == "Port Scan":
            latest_metrics["port_scan"] += 1
            log_alert(src_ip, dst_ip, str(proto), length, attack_type, "Medium")


def start_sniffing():
    # Run sniff in a separate background thread so it doesn't block the Flask webserver
    t = threading.Thread(target=lambda: sniff(prn=process_packet, store=False))
    t.daemon = True
    t.start()