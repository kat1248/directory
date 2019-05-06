#!/usr/bin/python

import os
import tempfile
import csv, sys, getopt

def main(argv):
    emails = []
    with open('email.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row.get('Email', "")
            if email != "":
                emails.append(email)
    with open('email_list.txt', 'w') as out_file:
        count = 0
        for e in sorted(emails):
            count += 1
            out_file.write("{0}\n".format(e))
            if count == 45:
                out_file.write("===\n")
                count = 0
        
if __name__ == "__main__":
    main(sys.argv)