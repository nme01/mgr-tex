import os
from constants import OUT_DIRECTORY


if __name__ == "__main__":
    os.system("start " + os.path.join(OUT_DIRECTORY, "main.pdf"))
