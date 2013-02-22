'''
результат - объединенные строки из двух файлов с совпадающими id
'''
import time

start_ = time.time()
print "start = %s" % (start_)

in_ = open("train_wow.csv", "r")
idx1 = []
for line in in_.xreadlines():
    s = line.strip()
    s = s.split(";")
    idx1.append([long(s[0]),s])
in_.close()

in_ = open("uuu_train.csv", "r")
idx2 = []
for line in in_.xreadlines():
    s = line.strip()
    s = s.split(";")
    idx2.append([long(s[0]),s])
in_.close()

out_ = open("train_wow2.csv", "w")

for line1 in idx1:
    for line2 in idx2:
        if line1[0] == line2[0]:
            out_.write(";".join(line1[1])+";"+";".join(line2[1]) + "\n")

out_.close()

end_ = time.time()
print "all = %s" % (end_ - start_)

