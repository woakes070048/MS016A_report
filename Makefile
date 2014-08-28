# Makefile for compiling latex report
# Run make to compile report
# Run make clean to remove report and cclean to remove pdf as well
all: normal
cclean: clean rmpdf

normal:
	pdflatex report.tex
	bibtex report
	pdflatex report.tex
	pdflatex report.tex
	open report.pdf &

clean:
	rm -vf *.aux \
		*.bbl \
		*.blg \
		*.log \
		*.toc \
		*.out

rmpdf:
	rm -vf labreport.pdf
