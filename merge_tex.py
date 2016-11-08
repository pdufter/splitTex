import re
import os

# TODO make usable from command line

main_file = 'example_splitted.tex'

# parse file
with open(main_file, 'r') as f:
    # TODO test enocding
    data=f.read()


includes = re.findall(r'\\include{(.+?)}', data)

for includes in include:
    