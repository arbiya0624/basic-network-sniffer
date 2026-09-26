
from scapy.all import IP, TCP, UDP, ICMP, Raw, wrpcap, rdpcap

# Create sample packets
packet1 = IP(src="192.168.1.10", dst="192.168.1.20") / TCP(
    sport=12345, dport=80
) / Raw(load=b"HTTP request")

packet2 = IP(src="192.168.1.10", dst="8.8.8.8") / UDP(
    sport=54321, dport=53
) / Raw(load=b"DNS request")

packet3 = IP(src="192.168.1.10", dst="8.8.8.8") / ICMP()

packets = [packet1, packet2, packet3]

# Save packets
wrpcap("captured_packets.pcap", packets)

# Read packets
packets = rdpcap("captured_packets.pcap")

# Display packet information
for i, packet in enumerate(packets, start=1):

    print("=" * 60)
    print("Packet:", i)

    if IP in packet:
        print("Source IP       :", packet[IP].src)
        print("Destination IP  :", packet[IP].dst)

    if TCP in packet:
        print("Protocol        : TCP")
        print("Source Port     :", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)

    elif UDP in packet:
        print("Protocol        : UDP")
        print("Source Port     :", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)

    elif ICMP in packet:
        print("Protocol        : ICMP")

    print("Packet Length   :", len(packet), "bytes")
