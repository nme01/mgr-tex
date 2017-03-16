import os
from sys import platform

from constants import OUT_DIRECTORY


def open_pdf():
    if platform == "linux" or platform == "linux2":
        shell_cmd = "see"
    elif platform == "win32":
        shell_cmd = "start"
    else:
        raise ValueError("Unknown platform type: " + platform)

    path_to_pdf_file = os.path.join(OUT_DIRECTORY, "main.pdf")
    full_cmd = "".join([shell_cmd, " ", path_to_pdf_file])
    os.system(full_cmd)


if __name__ == "__main__":
    open_pdf()
