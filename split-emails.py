#!/usr/bin/python

import os
import csv, sys, getopt

section_length = 45
script_name = ''
input_file = ''
output_file = ''    

def parse_args(argv):
    global script_name, input_file, output_file
    script_name = argv[0]
    try:
        opts, args = getopt.getopt(argv[1:],"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print "{0} -i <inputfile> -o <outputfile>".format(script_name)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "{0} -i <inputfile> -o <outputfile>".format(script_name)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

def main():
    global input_file, output_file, section_length
    emails = []
    with open(input_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row.get('Email', '')
            if email != '':
                emails.append(email)
    with open(output_file, 'w') as out_file:
        count = 0
        for e in sorted(emails):
            count += 1
            out_file.write("{0}\n".format(e))
            if count == section_length:
                out_file.write("===\n")
                count = 0
        
if __name__ == "__main__":
    parse_args(sys.argv)
    main()