#!/usr/bin/python
# TODO:
# - get file names from command line
# - output current/alternate delegates info

import csv

def table_end(fh):
    fh.write("\\end{longtable}\n")

def print_header(fh, area_number, area_name):
    fh.write("\\newpage\n")
    fh.write("\\footnotesize\n")
    fh.write("\\begin{longtable}{|l|l|l|}\n")
    fh.write("\\caption{\\underline{" + "Area {0} --- {1}".format(area_number, area_name) + "}}\\\\\n")
    fh.write("\\hline\n")

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
    fh.write("\\newpage\n")
    fh.write("\\footnotesize\n")
    fh.write("\\begin{longtable}{|l|l|l|}\n")
    fh.write("\\caption{\\underline{Delegates from other Areas}}\\\\\n")
    fh.write("\\hline\n")
    for v in visitors:
        print_delegate(fh, v)
    table_end(fh)

valid_areas = ['11', '12', '13', '28', '29', '30', '31', '43', '44', '45', '47', '48', '49', '50', '59', '60', '61', '70']
current_panels = ['68', '69']
current_alts = ['Alt-68', 'Alt-69']

area = 0
dead = []
honorary = []
current = []
alternate = []

with open('delegates.tex', 'w') as del_file:
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

#print current
#print alternate