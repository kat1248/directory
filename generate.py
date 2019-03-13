#!/usr/bin/python

import csv

def table_end():
    print ("\\end{longtable}")

def print_header(area_number, area_name):
    print ("\\newpage")
    print ("\\footnotesize")
    #print ("\\begin{longtable}{@{\\extracolsep{\\fill}}|l|l|l|}")
    print ("\\begin{longtable}{|l|l|l|}")
    print ("\\caption{\\underline{" + "Area {0} --- {1}".format(area_number, area_name) + "}}\\\\")
    print ("\\hline")

def print_deceased(area_number, delegates):
    print ("\\large")
    print ("\\noindent")
    print ("\\textbf{\\underline{" + "Area {0} --- Past Delegates who are no longer with us:".format(area_number) + "}}")
    print ("\\footnotesize")
    print ("\\begin{description}")
    for d in delegates:
        print ("\\item[] {0} {1}, Panel {2}: Year Served {3} ({4})".format(d['First'], d['Last'], d['Panel'], d['Year Served'], area_number))
    print ("\\end{description}")

def print_delegate(d):
    if d['First'] == '':
        return
    print ("{0} {1} & Area {2}, Panel {3} & Tel: {4} \\\\*".format(d['First'], d['Last'], d['Area'], d['Panel'], d['Tel #']))
    print ("{0} & Year Served: {1} & Alt. Tel: {2} \\\\*".format(d['Street 1'], d['Year Served'], d['Alt Tel #']))
    if d['City'] == '':
        print (" & & Email: {0} \\\\*".format(d['Email']))
    else:
        print ("{0}, {1}, {2} & & Email: {3} \\\\*".format(d['City'], d['State'], d['Zip'], d['Email']))
    print ("\hline")

def print_visitors(visitors):
    print ("\\newpage")
    print ("\\footnotesize")
    print ("\\begin{longtable}{|l|l|l|}")
    print ("\\caption{\\underline{Delegates from other Areas}}\\\\")
    print ("\\hline")
    for v in visitors:
        print_delegate(v)
    table_end()

valid_areas = ['11', '12', '13', '28', '29', '30', '31', '43', '44', '45', '47', '48', '49', '50', '59', '60', '61', '70']

area = 0
dead = []
honorary = []
with open('main.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Area'] in valid_areas:
            if row['Area'] != area:
                if area != 0:
                    table_end()
                    print_deceased(area, dead)
                    dead = []
                print_header(row['Area'], row['Area Name'])
                area = row['Area']
            if row['Deceased'] == '':
                print_delegate(row)
            else:
                dead.append(row)
        else:
            honorary.append(row)
    
    table_end()
    print_deceased(area, dead)

    print_visitors(honorary)
