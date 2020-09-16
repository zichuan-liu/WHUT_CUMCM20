@echo off
color f9
pdflatex report
BibTex report
pdflatex report
pdflatex report
Call clean.bat
exit
