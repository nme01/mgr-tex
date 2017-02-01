#!/bin/bash
pdflatex tex/main.tex
bibtex "main"
pdflatex tex/main.tex
pdflatex tex/main.tex
