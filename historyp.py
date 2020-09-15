inp = "inH.txt"
oup = "outH.txt"


spl = []
with open(inp, "r") as f:
    spl = f.readlines()

with open(oup, "w") as f:
    for s in spl:
        text = "<tr>\n\t<td>\n"
        text += "\t\t{0}\n".format(s[:4])
        text += "\t</td>\n\t<td>\n"
        text += "\t\t{0}\n".format(s[13:])
        text += "\t</td>\n</tr>\n"
        f.write(text)


"""
<tr>\n
    \t<td>\n
        \t\ttext\n
    \t</td>\n
    \t<td>\n
        \t\ttext1\n
    \t</td>\n
</tr>\n
"""