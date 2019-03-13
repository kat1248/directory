template.pdf : delegates.tex template.tex
	pdflatex template.tex
	echo done

delegates.tex : main.csv generate.py
	echo generating delegates list
	python generate.py  > delegates.tex