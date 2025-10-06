# ETSI ITS CAM & DENM Packet Parser

A Python CLI tool to parse **Cooperative Awareness Messages (CAM)** and **Decentralized Environmental Notification Messages (DENM)** from ETSI ITS network captures (PCAP/PCAPNG) and export the extracted data to CSV for further analysis.

## Features
- Parses **CAM** and **DENM** messages from ETSI ITS PCAP/PCAPNG captures
- Extracts key information such as:
  - Packet timestamp
  - Station ID
  - Latitude and Longitude (converted to decimal degrees)
- Outputs results into a structured CSV file
- Lightweight and easy to integrate into ITS data analysis pipelines
- Built using [PyShark](https://github.com/KimiNewt/pyshark) (requires Wireshark/Tshark)

## Requirements
- Python 3.7+
- [Tshark](https://www.wireshark.org/docs/man-pages/tshark.html) installed on your system
- Python dependencies:
```bash
pip install pyshark
```

## Usage
Run the script with a PCAP/PCAPNG capture file:
```bash
python main.py input.pcapng -o output.csv
```

