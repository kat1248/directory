directory.pdf : delegates.tex directory.tex
	pdflatex directory.tex

delegates.tex : main.csv generate.py
	python generate.py delegates.tex current.tex

main.csv : raw.csv
	./repair.sh raw.csv main.csv

raw.csv : 
	rm -f raw.csv
	./fetch_data.sh

.PHONY: rerun
rerun:
	pdflatex directory.tex

all : directory.pdf

clean :
	rm -f main.csv directory.pdf raw.csv delegates.aux delegates.tex directory.aux directory.log
