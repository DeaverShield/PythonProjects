# Aaron Deaver

# Program to analyze log files of servers and workstations to identify issues

import os

def main():
    # Initialize five counters to 0
    critical_count = 0
    error_count = 0
    warning_count = 0
    info_count = 0
    add_count = 0  # Additional messages that do not fit any other category

    if not os.path.exists('program.log'):
        print("File program.log not found")
        return
# Open the program.log file. Did not encounter error so did not use try-except.
    with open('program.log', 'r') as file1:

# Develop if-elif-else construct

        for line in file1:
            message = line.split()
            if len(message) >= 4:
                error_type = message[3]

                if error_type == "CRITICAL":
                    critical_count += 1
                elif error_type == "ERROR":
                    error_count += 1
                elif error_type == "WARNING":
                    warning_count += 1
                elif error_type == "INFO":
                    info_count += 1
                else:
                    add_count += 1
# Display the count of log messages for each category

    print(f"CRITICAL: {critical_count}")
    print(f"ERROR:  {error_count}")
    print(f"WARNING:  {warning_count}")
    print(f"INFO:  {info_count}")
    print(f"UNKNOWN:  {add_count}")


main()
