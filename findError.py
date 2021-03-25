#!/usr/bin/env python3

import re
import csv
import operator

# Read the syslog file
f = open("syslog.log")
data = f.read()
f.close()

# Split the data string into a list of log messages
logList = data.split("\n")

# Initilize list of users and error messages
users = []
error_messages = []
# Loop over the log file and extract the error messages and users
for error in logList:
    result = re.search(r'ticky: ERROR ([\w \']*) \(([\w\.]*)\)', error)
    if result is not None:
        users.append(result.group(2))
        error_messages.append(result.group(1))

# Count occurences of type of error messages
error_type_counts = {}
for error_message in error_messages:
    if error_message in error_type_counts:
        error_type_counts[error_message] += 1
    else:
        error_type_counts[error_message] = 1
# Sort the count in descending order
error_type_counts_sorted = sorted(error_type_counts.items(), key = operator.itemgetter(1), reverse = True)
# print(error_type_counts_sorted)

users_error_count = {}
for user in users:
    if user in users_error_count:
        users_error_count[user] += 1
    else:
        users_error_count[user] = 1

# Sort by user
per_user = sorted(users_error_count.items(), key = operator.itemgetter(0))
#print(per_user)

users_info = []
for info in logList:
    result = re.search(r"ticky: INFO ([\w ]*)\[\#\d+\] \(([\w\.]*)\)", info)
    if result is not None:
        users_info.append(result.group(2))

users_info_counts = {}
for user in users_info:
    if user in users_info_counts:
        users_info_counts[user] += 1
    else:
        users_info_counts[user] = 1

# Sort by user
per_user_info = sorted(users_info_counts.items(), key = operator.itemgetter(0))
#print(per_user_info)

# Iterate through per_user and per_user_info to combine the error and info into 
# one dictionary
from collections import defaultdict
dd = defaultdict(list)
d1 = dict(per_user_info)
d2 = dict(per_user)
for d in (d1, d2):
    for key, value in d.items():
        if key in d1 and key in d2:
            dd[key].append(value)
        elif key in d1 and key not in d2:
            dd[key].extend([value,0])
        else:
            dd[key].extend([0, value])

dd = dict(dd)
# Sort dd by user
dd = sorted(dd.items(), key = operator.itemgetter(0))
#print((dd))

# Append records to a sorted list
sorted_users = []
for record in dd:
    sorted_users.append([record[0], record[1][0], record[1][1]])

sorted_users.insert(0,["Username","INFO","ERROR"])
error_type_counts_sorted.insert(0,["Error","Count"])

# Print to test
print(sorted_users)

with open("users_records.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(sorted_users)
    f.close()

with open("errors.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(error_type_counts_sorted)
    f.close()

