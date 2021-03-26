#!/bin/bash



grep 'Failed password for invalid' /var/log/secure*   | awk '{print $13}' | sort | uniq -c  |sort -n -k 1
