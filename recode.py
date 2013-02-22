"""

a;b;c;d
e;v;d;w
r;h;d;d
e;v;d;q

->

a;b;c;1
e;v;d;2
r;h;d;1
e;v;d;3


"""

import time
import zlib
import copy

my_index = 3 # номер столбца, который кодируем
start_ = time.time()
print "start = %s" % (start_)

in_ = open("u.csv", "r")
idx = []
unic = []
for line in in_.xreadlines():
    l = line.strip().split(";")
    zn = zlib.crc32(l[my_index]) 
    l[my_index] =  zn
    unic.append(zn)
    idx.append(l)
in_.close()

unic = list(set(unic))

out_ = open("u_out.csv", "w")
for x in idx:
    x[my_index] = str(unic.index(x[my_index]))
    out_.write(";".join(x)+"\n")

out_.close()
end_ = time.time()

print "all = %s" % (end_ - start_)

