.DEFAULT_GOAL := all
LATEX := pdflatex

OUTPUTS = directory.pdf current.pdf alternate.pdf
INCLUDES = $(patsubst %.pdf, %.inc.tex, $(OUTPUTS))

%.pdf : %.tex %.inc.tex
	$(LATEX) $<

$(INCLUDES) : main.csv generate.py 
	python generate.py

main.csv : raw.csv
	./repair.sh raw.csv main.csv

raw.csv : 
	./fetch_data.sh

.PHONY: rerun
rerun:
	$(LATEX) directory.tex

.PHONY: all
all : $(OUTPUTS) $(INCLUDES)
	@echo done

clean :
	echo $(INCLUDES)
	$(RM) -f  *.pdf *.csv *.inc.tex *.aux *.log *.fls *.fdb_latexmk *.gz 
