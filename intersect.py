"""
4101519751,1942428241 2461664561 955068058 1149825431 2352727660 4232243741 2281345341 3598630512 576339511 
2163304477,3369949871 3473964934 478577931 1623834088 1221225518 2429634045 1043755398

->

4101519751;346 (пересечение id's с другими id's в строках)
2163304477;236

"""

import time
import copy

start_ = time.time()
print "start = %s" % (start_)

in_ = open("user_train_sel.csv", "r")
rr = []
for line in in_.xreadlines():
    li = line.strip().split(",")
    zn = long(li[0])
    set1 = set(li[1].split(" "))
    rr.append([False, zn, set1, 0])

in_.close()

le = len(rr)

for x in xrange(le):
    for y in xrange(le):

        xx = copy.copy(rr[x])
        yy = copy.copy(rr[y])

        if (xx[0] == True) or (xx[1] == yy[1]):
            continue

        d1 = len(xx[2].intersection(yy[2]))

        rr[x][3] += d1 
        rr[y][3] += d1 

    rr[x][0] = True    

out_ = open("uuu_train.csv", "w")

for x in rr:
    out_.write(str(x[1])+";"+str(x[3])+"\n")

out_.close()

end_ = time.time()
print "all = %s" % (end_ - start_)

