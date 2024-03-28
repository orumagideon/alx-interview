#!/usr/bin/python3
"""
Script: Reads lines from standard input and calculates statistics
"""


def parseLogs():
    """
    Reads logs from standard input and produces reports
    Reports:
        * Displays log size after processing every 10 lines & upon KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles and re-raises this exception
    """
    stdin = __import__('sys').stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:
                fileSize += int(line[-1])
                if line[-2] in codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
        report(fileSize, statusCodes)
    except KeyboardInterrupt as e:
        report(fileSize, statusCodes)
        raise


def report(fileSize, statusCodes):
    """
    Prints the generated report to standard output
    Args:
        fileSize (int): total log size after every successful processing of 10 lines
        statusCodes (dict): dictionary containing status codes and their counts
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    parseLogs()
