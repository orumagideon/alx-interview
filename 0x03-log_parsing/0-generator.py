#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

def generate_logs():
    """
    Generates logs with random data and writes them to standard output
    """
    for _ in range(10000):
        sleep(random.random())
        sys.stdout.write(f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)} - [{datetime.datetime.now()}] \"GET /projects/260 HTTP/1.1\" {random.choice([200, 301, 400, 401, 403, 404, 405, 500])} {random.randint(1, 1024)}\n")
        sys.stdout.flush()

if __name__ == '__main__':
    generate_logs()
