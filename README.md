# Basic Network Sniffer

## Overview

This project demonstrates basic network packet analysis using Python and Scapy.

The project analyzes sample network packets stored in a PCAP file and identifies important packet information.

## Features

- Analyze network packets
- Display source IP address
- Display destination IP address
- Identify protocols
- Display TCP and UDP ports
- Display packet length
- Save packet data in PCAP format
- Export packet analysis to CSV

## Technologies Used

- Python
- Scapy
- Google Colab
- PCAP
- CSV

## Protocols Demonstrated

- TCP
- UDP
- ICMP

## Output

Example packet analysis:

Packet 1:
- Source IP: 192.168.1.10
- Destination IP: 192.168.1.20
- Protocol: TCP

Packet 2:
- Source IP: 192.168.1.10
- Destination IP: 8.8.8.8
- Protocol: UDP

Packet 3:
- Source IP: 192.168.1.10
- Destination IP: 8.8.8.8
- Protocol: ICMP

## Project Files

- `network_sniffer.py` - Python source code
- `captured_packets.pcap` - Sample packet capture
- `packet_analysis.csv` - Packet analysis results
- `README.md` - Project documentation

## Conclusion

This project demonstrates basic network packet analysis using Python and Scapy.
