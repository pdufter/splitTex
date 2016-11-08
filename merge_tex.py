import re
import os

# TODO make usable from command line

main_file = 'example_splitted.tex'

# parse file
with open(main_file, 'r') as f:
    # TODO test enocding
    data=f.read()


includes = re.findall(r'\\include{(.+?)}', data)

for include in includes:
    with open(include + ".tex", 'r') as f:
        # TODO test enocding
        section = f.read()
    data = re.sub(r'\\include{' + include + '}', section, data)



with open(re.sub(".tex", "_merged.tex", main_file), 'w') as f:
    f.write(data)