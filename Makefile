directory.pdf : delegates.tex directory.tex generate.py
	pdflatex directory.tex

delegates.tex : main.csv generate.py
	python generate.py delegates.tex current.tex

main.csv : raw.csv
	./repair.sh raw.csv main.csv

raw.csv : 
	./fetch_data.sh

.PHONY: rerun
rerun:
	pdflatex directory.tex

all : directory.pdf

clean :
	$(RM) -f  *.pdf *.csv delegates.tex *.aux *.log *.fls *.fdb_latexmk *.gz
