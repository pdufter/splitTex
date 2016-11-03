import re
import os

# parse file
with open('example.tex') as f:
    # TODO improve parsing
    # TODO test enocding
    data=f.read().replace('\n', '')

# get document 
document = re.split(r"\{document\}", data)[1]


sections = re.split(r"\\section\{(.+?)\}", data)[1:]


directory = "content"
if not os.path.exists(directory):
    os.makedirs(directory)
else:
    raise ValueError("Directory 'content' exists already.")

for i in range(0, len(sections) / 2):
    with open(directory + "/" + sections[2 * i] + ".tex", "w") as f:
        # TODO formatting is broke obviously
        f.write("\section{" + sections[2 * i] + "}" + sections[2 * i + 1])