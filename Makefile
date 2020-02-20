.DEFAULT_GOAL := all

LATEX := pdflatex
PYTHON := python
FETCH := ./fetch_data.sh
CP := cp
SORT := csvsort

OUTPUTS = directory.pdf current.pdf alternate.pdf
INCLUDES = $(patsubst %.pdf, %.inc.tex, $(OUTPUTS))
DATE_STAMP = $(shell date +%Y-%m-%d)
COPY_FILES = $(patsubst %.pdf, %-$(DATE_STAMP).pdf, $(OUTPUTS))

PANELS = "\\newcommand\{\\panelA\}\{69 \}\\newcommand\{\\panelB\}\{70\}"
NEXT_PANELS = "\\newcommand\{\\panelA\}\{69 \}\\newcommand\{\\panelB\}\{70\}"

current.pdf : page.tex current.inc.tex
	$(LATEX) -jobname current "\newcommand{\includedFile}{current.inc}\newcommand{\includedTitle}{Delegates}${PANELS}\input{$<}"

alternate.pdf : page.tex alternate.inc.tex
	$(LATEX) -jobname alternate "\newcommand{\includedFile}{alternate.inc}\newcommand{\includedTitle}{Alternate Delegates}${PANELS}\input{$<}"

next.pdf : page.tex current.inc.tex
	$(LATEX) -jobname next "\newcommand{\includedFile}{current.inc}\newcommand{\includedTitle}{Delegates}${NEXT_PANELS}\input{$<}"

next-alternate.pdf : page.tex alternate.inc.tex
	$(LATEX) -jobname next-alternate "\newcommand{\includedFile}{alternate.inc}\newcommand{\includedTitle}{Alternate Delegates}${NEXT_PANELS}\input{$<}"

incoming : next.pdf next-alternate.pdf

directory.pdf : directory.tex directory.inc.tex
	$(LATEX) $<

$(INCLUDES) : main.csv generate.py 
	$(PYTHON) generate.py

main.csv emails.csv : 
	$(FETCH) del.csv emails.csv
	$(SORT) -c Area,Panel del.csv > main.csv
	$(RM) del.csv

emails.txt : emails.csv
	$(PYTHON) split-emails.py -i $< -o $@

.PHONY : rerun
rerun :
	$(LATEX) directory.tex

.PHONY : all
all : $(OUTPUTS) $(INCLUDES) emails.txt
	@echo built

clean :
	$(RM) -f  *.pdf *.csv *.inc.tex *.aux *.log *.fls *.fdb_latexmk *.gz *.txt

.PHONY : distribute
distribute : $(COPY_FILES)
	@echo timestamped

%-$(DATE_STAMP).pdf: %.pdf
	@$(CP) $< $@
