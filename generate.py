import os
from subprocess import call

OUT_DIRECTORY = "out"


def create_output_dir() -> bool:
    if not os.path.exists(OUT_DIRECTORY):
        os.makedirs(OUT_DIRECTORY)
    return True


def generate_pdf() -> bool:
    return call(["pdflatex", "-output-directory", "out", "tex/main.tex"]) == 0


def generate_bibliography() -> bool:
    return call(["bibtex", "out/main"]) == 0


ret_code = create_output_dir() \
           and generate_pdf() \
           and generate_bibliography() \
           and generate_pdf() \
           and generate_pdf()
