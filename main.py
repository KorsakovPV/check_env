import glob
import os
from string import ascii_uppercase


def check_environment():
    for file in glob.glob(f'**/.env.template', recursive=True):
        with open(file) as f:
            while line := f.readline():
                if line[0] in ascii_uppercase:
                    if not os.getenv(f"{line.split('=')[0].strip()}"):
                        raise Exception(f"{line.split('=')[0].strip()} is None")
                        # print(f"{line.split('=')[0].strip()} is None")


if __name__ == '__main__':
    check_environment()
