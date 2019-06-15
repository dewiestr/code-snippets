#!/usr/bin/python
from __future__ import print_function
import json
import csv
import argparse

def process(INPUT_FILE,OUTPUT_FILE):
    """
        Takes input files as individual lines of json and puts them as a CSV file for excel integration. the first line needs to have all the correct headers otherwise this fails. 
        TODO: update so we get all keyfiles from every line to create the column headers. 
    """
    count = 0
    csvwriter = csv.writer(OUTPUT_FILE)
    for line in INPUT_FILE:
        if count == 0:
            first_line = json.loads(line)
            csvwriter.writerow(first_line.keys())
            csvwriter.writerow(first_line.values())
            count +=1
        csvwriter.writerow(json.loads(line).values())
    return 

def main():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "input", nargs="?", default="-",
        metavar="INPUT_FILE", type=argparse.FileType("r"),
        help="path to the input file (read from stdin if omitted)")

    parser.add_argument(
        "output", nargs="?", default="-",
        metavar="OUTPUT_FILE", type=argparse.FileType("w"),
        help="path to the output file (write to stdout if omitted)")

    args = parser.parse_args()
    process(args.input,args.output)

if __name__ == "__main__":
    main()
