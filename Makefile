.DEFAULT_GOAL := all

LATEX := pdflatex
PYTHON := python
FETCH := ./fetch_data.sh

OUTPUTS = directory.pdf current.pdf alternate.pdf
INCLUDES = $(patsubst %.pdf, %.inc.tex, $(OUTPUTS))

current.pdf : page.tex current.inc.tex
	$(LATEX) -jobname current "\newcommand{\includedFile}{current.inc}\newcommand{\includedTitle}{Delegates}\input{$<}"

alternate.pdf : page.tex alternate.inc.tex
	$(LATEX) -jobname alternate "\newcommand{\includedFile}{alternate.inc}\newcommand{\includedTitle}{Alternate Delegates}\input{$<}"

directory.pdf : directory.tex directory.inc.tex
	$(LATEX) $<

$(INCLUDES) : main.csv generate.py 
	$(PYTHON) generate.py

main.csv emails.csv : 
	$(FETCH) main.csv emails.csv

emails.txt : emails.csv
	$(PYTHON) split-emails.py -i $< -o $@

.PHONY : rerun
rerun :
	$(LATEX) directory.tex

.PHONY : all
all : $(OUTPUTS) $(INCLUDES) emails.txt
	@echo done

clean :
	$(RM) -f  *.pdf *.csv *.inc.tex *.aux *.log *.fls *.fdb_latexmk *.gz *.txt
