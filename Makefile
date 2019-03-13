template.pdf : delegates.tex template.tex
	pdflatex template.tex

delegates.tex : main.csv generate.py
	python generate.py  > delegates.tex

main.csv : raw.csv
	./repair.sh raw.csv main.csv
