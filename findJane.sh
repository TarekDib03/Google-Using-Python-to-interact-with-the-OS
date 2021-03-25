#!/bin/bash

# Create an empty file oldFiles.txt using >
>oldFiles.txt
# Append the files developed by jane using >>
grep ' jane ' list.txt | cut -d ' ' -f 3 >> oldFiles.txt