"""
a;b
1;2
+
5
->
a;b;r
1;2;5

"""

import time

start_ = time.time()
print "start = %s" % (start_)

in_ = open("rrr_.csv", "r")
idx = []
for line in in_.xreadlines():
    idx.append(line.strip())
in_.close()

in_ = open("t.csv", "r")
out_ = open("test_v20.csv", "w")

k = 0
o = 0
for line in in_.xreadlines():
    if o == 0:
        out_.write(line.strip()+";r\n")
        o += 1
    else:
        out_.write(line.strip()+";"+idx[k]+"\n")
        k = k + 1

out_.close()
in_.close()

end_ = time.time()
print "all = %s" % (end_ - start_)

