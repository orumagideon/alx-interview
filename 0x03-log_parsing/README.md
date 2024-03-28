# 0x03. Log Parsing

## Overview
This project focuses on creating a Python script for parsing and processing log data in real-time from standard input (stdin). The script reads input line by line, computes metrics, and prints statistics at regular intervals or upon keyboard interruption.

### Project Details
- **Start Date:** March 25, 2024 6:00 AM
- **End Date:** March 29, 2024 6:00 AM
- **Checker Release Date:** March 26, 2024 6:00 AM
- **Auto Review:** Launched at the deadline

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- PEP 8 style (version 1.7.x)
- All files must be executable
- Length of files will be tested using `wc`

## Tasks
### Task 0: Log Parsing
Write a script that reads stdin line by line, parses log entries, and computes metrics as specified in the project description.

#### Input Format
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

markdown
Copy code
- Lines not following this format should be skipped.

#### Metrics
- After every 10 lines and/or a keyboard interruption (CTRL + C), print statistics:
  - Total file size: `File size: <total size>`
  - Number of lines by status code:
    - Status codes: 200, 301, 400, 401, 403, 404, 405, 500
    - Format: `<status code>: <number>`
    - Status codes should be printed in ascending order

### Additional Resources
- Mock Technical Interview

## Implementation
The script `0-stats.py` parses log entries, calculates statistics, and prints metrics as specified in the project requirements.

## Directory Structure
alx-interview/
└── 0x03-log_parsing/
├── 0-generator.py
└── 0-stats.py

markdown
Copy code

## Usage
1. Ensure Python 3 is installed.
2. Execute the `0-generator.py` script to generate sample log data.
3. Pipe the output of `0-generator.py` to the `0-stats.py` script.
4. View the computed metrics printed to the terminal.

## Contributors
- [orumagideon](https://github.com/orumagideon) 
