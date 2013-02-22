import time
import copy

start_ = time.time()
print "start = %s" % (start_)

out_ = open("super_l3.csv", "w")
in_ = open("super_recode.csv", "r")
for line in in_.xreadlines():
    s = line.strip()
    s = s.split(";")
    r = copy.copy(s[3:6])
    del s[3:6]
    out_.write(";".join(s)+";"+";".join(r)+"\n")
in_.close()
out_.close()
end_ = time.time()
print "all = %s" % (end_ - start_)

