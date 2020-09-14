inp = "in.txt"
oup = "out.txt"
tag ="<p>"
tag_end="</p>"

spl = []
with open(inp, "r") as f:
    spl = f.readlines()

with open(oup, "w") as f:
    for s in spl:
        while s != "\n":
            d = s.find("[")
            if d != -1:
               s = s[:d]+ s[s.find("]")+1]
            else:
                f.write(tag+s+tag_end+"\n")
                break