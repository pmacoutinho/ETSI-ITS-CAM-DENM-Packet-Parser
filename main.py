#!/usr/bin/env python3
"""
Extract CAM info from an ETSI ITS pcap and save to CSV.

Requirements:
    pip install pyshark
    # and make sure tshark is installed on the system

Run:
    python3 parse_packets.py input.pcapng -o output.csv
"""

import csv
import pyshark
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Extract CAM info from an ETSI ITS pcap and save to CSV."
    )
    parser.add_argument("input_file", help="Path to the input pcap/pcapng file")
    parser.add_argument(
        "-o",
        "--output",
        default="cam_packets.csv",
        help="Path to the output CSV file (default: cam_packets.csv)",
    )

    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output

    # Open capture
    try:
        cap = pyshark.FileCapture(input_file)
    except Exception as e:
        print(f"Error opening capture file: {e}")
        sys.exit(1)

    rows = []

    for pkt in cap:
        # skip if no ITS layer
        if not hasattr(pkt, "its"):
            continue

        ts = pkt.sniff_time.isoformat()

        station_id = getattr(pkt.its, "stationid", None)

        # latitude / longitude (if available)
        lat_raw = getattr(pkt.its, "latitude", None)
        lon_raw = getattr(pkt.its, "longitude", None)

        if lat_raw is not None and lon_raw is not None:
            # Convert from 0.1 micro-degree to decimal degrees
            lat_deg = int(lat_raw) / 10_000_000
            lon_deg = int(lon_raw) / 10_000_000
        else:
            # If missing, store as None
            lat_deg = None
            lon_deg = None

        rows.append(
            {
                "timestamp": ts,
                "station_id": station_id,
                "latitude_deg": lat_deg,
                "longitude_deg": lon_deg,
            }
        )

    cap.close()

    # Save to CSV
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "timestamp",
                "station_id",
                "latitude_deg",
                "longitude_deg",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Extracted {len(rows)} CAM packets → saved to {output_file}")


if __name__ == "__main__":
    main()
