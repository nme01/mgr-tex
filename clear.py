import os
import shutil

from constants import OUT_DIRECTORY


def clear():
    for the_file in os.listdir(OUT_DIRECTORY):
        file_path = os.path.join(OUT_DIRECTORY, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    clear()
