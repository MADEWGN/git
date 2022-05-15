import os
import sys

# show file list whitout 'HEAD', 'hooks', 'info', 'objects', 'refs', 'description', 'config'
def show_file(path):
    for file in os.listdir(path):
        if file != 'HEAD' and file != 'hooks' and file != 'info' and file != 'objects' and file != 'refs' and file != 'description' and file != 'config':
            print(file)

show_file("repos/aaa")
