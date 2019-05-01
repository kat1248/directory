.DEFAULT_GOAL := all
LATEX := pdflatex

OUTPUTS = directory.pdf current.pdf alternate.pdf
INCLUDES = $(patsubst %.pdf, %.inc.tex, $(OUTPUTS))

current.pdf: page.tex current.inc.tex
	$(LATEX) -jobname current "\newcommand{\includedFile}{current.inc}\newcommand{\includedTitle}{Delegates}\input{$<}"

alternate.pdf: page.tex alternate.inc.tex
	$(LATEX) -jobname alternate "\newcommand{\includedFile}{alternate.inc}\newcommand{\includedTitle}{Alternate Delegates}\input{$<}"

directory.pdf: directory.tex directory.inc.tex
	$(LATEX) $<

$(INCLUDES) : main.csv generate.py 
	python generate.py

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
