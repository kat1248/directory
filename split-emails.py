#!/usr/bin/python

import os
import csv, sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''    
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    emails = []
    with open(inputfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row.get('Email', "")
            if email != "":
                emails.append(email)
    with open(outputfile, 'w') as out_file:
        count = 0
        for e in sorted(emails):
            count += 1
            out_file.write("{0}\n".format(e))
            if count == 45:
                out_file.write("===\n")
                count = 0
        
if __name__ == "__main__":
    main(sys.argv[1:])