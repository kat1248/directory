.DEFAULT_GOAL := all
LATEX := pdflatex
PYTHON := python

OUTPUTS = directory.pdf current.pdf alternate.pdf
INCLUDES = $(patsubst %.pdf, %.inc.tex, $(OUTPUTS))

%.pdf : page.tex %.inc.tex
	$(LATEX) -jobname $* "\newcommand{\includedFile}{current.inc}\newcommand{\includedTitle}{Delegates}\input{$<}"

directory.pdf: directory.tex directory.inc.tex
	$(LATEX) $<

$(INCLUDES) : main.csv generate.py 
	$(PYTHON) generate.py

main.csv : 
	./fetch_data.sh $@

.PHONY: rerun
rerun:
	$(LATEX) directory.tex

.PHONY: all
all : $(OUTPUTS) $(INCLUDES)
	@echo done

clean :
	$(RM) -f  *.pdf *.csv *.inc.tex *.aux *.log *.fls *.fdb_latexmk *.gz 
