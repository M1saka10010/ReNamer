import os
from pydoc import ispath
from uuid import uuid4
import sys


def rename_files(dir):
    for file in os.listdir(dir):
        if not file.endswith('.py'):
            os.rename(dir + file, dir + str(uuid4()) +
                      os.path.splitext(os.path.abspath(file))[-1])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if ispath(arg):
                if arg.split('/')[-1] == '':
                    rename_files(arg)
                else:
                    rename_files(arg + '/')
            else:
                print(f'{arg} is not a path')
    else:
        rename_files('./')
