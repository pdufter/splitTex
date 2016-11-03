import re
import os

# TODO make usable from command line

original_file = 'example.tex'

# parse file
with open(original_file, 'r') as f:
    # TODO test enocding
    data=f.read()

# get document 
data = re.split(r"\\begin{document}", data)
head = data[0]
data = re.split(r"\\end{document}", data[1])
document = data[0]
footer = data[1]

# TODO make section selection flexible
sections = re.split(r"\\section\{(.+?)\}", document)
section_0 = sections[0]
sections = sections[1:]

mainfile = head + "\\begin{document}\n" + section_0



directory = "content"
if not os.path.exists(directory):
    os.makedirs(directory)
else:
    # TODO add option to overwrite
    raise ValueError("Directory 'content' exists already.")

for i in range(0, len(sections) / 2):
    filename = directory + "/" + re.sub(" ", "_", sections[2 * i]) + ".tex"
    j = 2
    while os.path.isfile(filename):
        filename = directory + "/" + sections[2 * i] + "_" + str(j) + ".tex"
    mainfile = mainfile + "\include{" + re.sub(".tex", "", filename) + "}\n"

    with open(filename, "w") as f:
        # TODO formatting is broke obviously
        f.write("\section{" + sections[2 * i] + "}" + sections[2 * i + 1])



mainfile = mainfile + footer + "\end{document}"

with open(re.sub(".tex", "_splitted.tex", original_file), 'w') as f:
    f.write(mainfile)
