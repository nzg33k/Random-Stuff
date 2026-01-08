"""Take a list of DNS hosts and check for hosts with mismatched reverse records"""

import csv
import socket

CSV_FILENAME = "zone.csv"
OUTFILE = "reverse_checks_results.txt"
with open(OUTFILE,'w', encoding='utf-8') as results:
    with open(CSV_FILENAME, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == 'arecord':
                try:
                    reverse_hostname = socket.gethostbyaddr(row[1])
                except socket.herror:
                    results.write(f"{row[3]}'s ip {row[1]} did not resolve")
                else:
                    short_reverse_hostname = reverse_hostname[0].split(".")[0]
                    short_hostname = row[3].split(".")[0]
                    if short_reverse_hostname != short_hostname:
                        results.write(f"reverse result {short_reverse_hostname}" +
                                      " is not the same as the zone hostname {short_hostname}\n")
        csvfile.close()
    results.close()
