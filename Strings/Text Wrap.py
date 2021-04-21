def wrap(string, max_width):
    x = textwrap.wrap(string, max_width)
    z = ""
    for y in x :
        z += "{}{}".format(y,"\n")
    return z
