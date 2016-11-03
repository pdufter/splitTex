

# parse file
with open('example.tex') as f:
    # todo 
    data=f.read().replace('\n', '')
    print data