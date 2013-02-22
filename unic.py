"""
in1 = open("v_u_3.csv", "r")
ou1 = open("v_u_3_.csv", "w")

for s in in1.xreadlines():
    s = s.strip()
    if s == "nan":
        s = 0
    ou1.write("%s\n" % s)

in1.close()
ou1.close() 

exit()
"""

import time
import numpy as np
def count_unique(keys):
    uniq_keys = np.unique(keys)
    bins = uniq_keys.searchsorted(keys)
    return uniq_keys, np.bincount(bins)

start_ = time.time()
x = np.genfromtxt('v_u_4.csv')
# x = np.array([1,1,1,2,2,2,5,25,1,1])

rr = count_unique(x)

# np.savetxt("zn.csv", rr[0], fmt='%i.0')
# np.savetxt("co.csv", rr[1], fmt='%i.0')

in1 = open("zn.csv", "w") # уник. значения
in2 = open("co.csv", "w") # их кол-во

for x in rr[0]:
    x = '%.0f\n' % x
    in1.write(x)

for x in rr[1]:
    x = '%.0f\n' % x
    in2.write(x)

in1.close()
in2.close()

end_ = time.time()

print "all = %s\n" % (end_ - start_)
