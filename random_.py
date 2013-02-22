import time
import random

start_ = time.time()
print "start = %s" % (start_)

random.seed(time.time())

in_ = open("ee_full.csv", "r")
out_ = open("random_ee_full.csv", "w")

k = 0
for line in in_.xreadlines():
    if random.random() < 0.25:
        out_.write(line)
        k += 1
        if k >= 40000:
            break
in_.close()
out_.close()

end_ = time.time()
print "all = %s" % (end_ - start_)

