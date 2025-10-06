# ETSI ITS CAM & DENM Packet Parser

A Python CLI tool to parse **Cooperative Awareness Messages (CAM)** and **Decentralized Environmental Notification Messages (DENM)** from ETSI ITS network captures (PCAP/PCAPNG) and export the extracted data to CSV for further analysis.

The project is containerized with Docker to avoid dealing with Python or Tshark installation locally.

## Features
- Parses **CAM** and **DENM** messages from ETSI ITS PCAP/PCAPNG captures
- Extracts key information such as:
  - Packet timestamp
  - Station ID
  - Latitude and Longitude (converted to decimal degrees)
- Outputs results into a structured CSV file
- Lightweight and easy to integrate into ITS data analysis pipelines
- Built using [PyShark](https://github.com/KimiNewt/pyshark) (requires Wireshark/Tshark)

## 📦 Prerequisites
### Running with Docker
You need **Docker** installed and running on your system.
1. Install and enable Docker:
```bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
```

2. Build the Docker Image
```bash
docker build -t cam-denm-parser .
```

### Running Locally
- Python 3.7+
- [Tshark](https://www.wireshark.org/docs/man-pages/tshark.html) installed on your system
- Install Python 3.11+ and Tshark:
```bash
sudo apt-get install tshark
pip install -r requirements.txt
```

## Usage
### Running with Docker
```bash
docker run --rm \
  -v $(pwd)/testdata:/testdata \
  -v $(pwd)/results:/results \
  cam-denm-parser /testdata/input.pcap -o /results/output.csv
```

### Running locally
Run the script with a PCAP/PCAPNG capture file:
```bash
python main.py input.pcapng -o output.csv
```

## Results
An example output would be:
```csv
timestamp,station_id,latitude_deg,longitude_deg
2025-10-06T14:32:18.123Z,1234,40.1234567,-8.6543210
2025-10-06T14:32:18.456Z,5678,40.2345678,-8.7654321
```

