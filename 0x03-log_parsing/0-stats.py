#!/usr/bin/python3
""" This script reads from standard input and computes metrics """
import sys
import signal


# Initialize variables
total_size = 0
status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

# Function to print statistics
def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

# Signal handler for keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Attach the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) == 7 and parts[5].isdigit():
            total_size += int(parts[6])
            status_codes[parts[5]] += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

finally:
    print_stats()
