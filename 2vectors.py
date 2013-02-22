"""
12;2  ->

12*0.3+2

"""

in_ = open("qqq.csv", "r")
idx = []
for line in in_.xreadlines():
    s = line.strip().split(";")
    idx.append( float(s[0]) * 0.3 + float(s[1]) )
in_.close()

out_ = open("rrr_.csv", "w")

for x in idx:
    out_.write(str(x)+"\n")

out_.close()

