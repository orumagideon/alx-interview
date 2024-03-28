#!/usr/bin/python3
"""
Script: Reads lines from standard input and calculates statistics
"""

import sys
from collections import defaultdict

def parse_logs():
    """
    Reads logs from standard input and produces reports
    Reports:
        * Displays log size after processing every 10 lines & upon KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles and re-raises this exception
    """
    line_number = 0
    file_size = 0
    status_codes = defaultdict(int)
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in sys.stdin:
            line_number += 1
            line = line.split()
            try:
                file_size += int(line[-1])
                if line[-2] in codes:
                    status_codes[line[-2]] += 1
            except (IndexError, ValueError):
                pass
            if line_number % 10 == 0:
                report(file_size, status_codes)
        report(file_size, status_codes)
    except KeyboardInterrupt:
        report(file_size, status_codes)
        raise

def report(file_size, status_codes):
    """
    Prints the generated report to standard output
    Args:
        file_size (int): total log size after every successful processing of 10 lines
        status_codes (dict): dictionary containing status codes and their counts
    """
    print(f"File size: {file_size}")
    for key, value in sorted(status_codes.items()):
        print(f"{key}: {value}")

if __name__ == '__main__':
    parse_logs()
