#!/usr/bin/python
# TODO:
# - get file names from command line

import csv, sys, getopt
from datetime import date
from datetime import time
from datetime import datetime

use_longtabu = True

def table_start(fh):
    fh.write("\\newpage\n")
    fh.write("\\footnotesize\n")
    if use_longtabu:
        fh.write("\\begin{longtabu} to \\textwidth {|X[3,l]|X[3,l]|X[4,l]|}\n")
    else:
        fh.write("\\begin{longtable}{|l|l|l|}\n")

def table_caption(fh, caption):
    fh.write("\\caption{\\underline{" + caption + "}}\\\\\n")
    fh.write("\\hline\n")

def table_del_caption(fh):
    fh.write("\\hline\n")

def table_end(fh):
    if use_longtabu:
        fh.write("\\end{longtabu}\n")
    else:
        fh.write("\\end{longtable}\n")

def print_header(fh, area_number, area_name):
    table_start(fh)
    table_caption(fh, "Area {0} --- {1}".format(area_number, area_name))

def print_deceased(fh, area_number, delegates):
    fh.write("\\large\n")
    fh.write("\\noindent\n")
    fh.write("\\textbf{\\underline{" + "Area {0} --- Past Delegates who are no longer with us:".format(area_number) + "}}\n")
    fh.write("\\footnotesize\n")
    fh.write("\\begin{description}\n")
    for d in delegates:
        fh.write("\\item[] {0} {1}, Panel {2}: Year Served {3} ({4})".format(d['First'], d['Last'], d['Panel'], d['Year Served'], area_number))
    fh.write("\\end{description}\n")

def print_delegate(fh, d):
    if d['First'] == '':
        return
    fh.write("{0} {1} & Area {2}, Panel {3} & Tel: {4} \\\\*".format(d['First'], d['Last'], d['Area'], d['Panel'], d['Tel #']))
    fh.write("{0} & Year Served: {1} & Alt. Tel: {2} \\\\*".format(d['Street 1'], d['Year Served'], d['Alt Tel #']))
    if d['City'] == '':
        fh.write(" & & Email: {0} \\\\*".format(d['Email']))
    else:
        fh.write("{0}, {1}, {2} & & Email: {3} \\\\*".format(d['City'], d['State'], d['Zip'], d['Email']))
    fh.write("\hline\n")

def print_visitors(fh, visitors):
    table_start(fh)
    table_caption(fh, 'Delegates from other Areas')
    for v in visitors:
        print_delegate(fh, v)
    table_end(fh)

def print_current_delegates(fh, delegates):
    table_start(fh)
    table_del_caption(fh)
    for v in delegates:
        print_current(fh, v)
    table_end(fh)

def print_current(fh, d):
    area = "{0} - {1}".format(d['Area Name'], d['Area'])
    fh.write("\\textbf{\\underline{" +  area + "}} & " + "Panel {0} & Tel: {1} \\\\*".format(d['Panel'], d['Tel #']))
    fh.write("{0} {1} & Year Served {2} & Alt. Tel: {3} \\\\*".format(d['First'], d['Last'], d['Year Served'], d['Alt Tel #']))
    fh.write("{0} & & Email: {1} \\\\*".format(d['Street 1'], d['Email']))
    if d['City'] == '':
        fh.write(" & & \\\\*")
    else:
        fh.write("{0}, {1}, {2} & & \\\\*".format(d['City'], d['State'], d['Zip']))
    fh.write("\hline\n")

def main(argv, panel):
    valid_areas = ['11', '12', '13', '28', '29', '30', '31', '43', '44', '45', '47', '48', '49', '50', '59', '60', '61', '70']
    current_panels = [str(panel), str(panel + 1)]
    current_alts = ['Alt-' + str(panel), 'Alt-' + str(panel + 1)]

    area = 0
    dead = []
    honorary = []
    current = []
    alternate = []

    with open('directory.inc.tex', 'w') as del_file:
        with open('main.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Area'] in valid_areas:
                    if row['Area'] != area:
                        if area != 0:
                            table_end(del_file)
                            print_deceased(del_file, area, dead)
                            dead = []
                        area = row['Area']
                        print_header(del_file, area, row['Area Name'])
                    if row['Deceased'] == '':
                        print_delegate(del_file, row)
                        if row['Panel'] in current_panels:
                            current.append(row)
                        elif row['Panel'] in current_alts:
                            alternate.append(row)
                    else:
                        dead.append(row)
                else:
                    honorary.append(row)
        
        table_end(del_file)
        print_deceased(del_file, area, dead)

        print_visitors(del_file, honorary)

    with open('current.inc.tex', 'w') as cur_file:
        print_current_delegates(cur_file, current)

    with open('alternate.inc.tex', 'w') as alt_file:
        print_current_delegates(alt_file, alternate)

if __name__ == "__main__":
    today = date.today()
    panel = today.year - 1950
    main(sys.argv, panel - 1)