"""
user;event;r
3369635310;165954795;0.255901265
3369635310;749859087;0.153918915
3369635310;1767325091;0.090146368
3369635310;2038842201;0.028517603
3369635310;2583998307;0.197756473
3369635310;3199229320;0.041234243
3369635310;3769851269;0.08655942
3369635310;3790866767;0.140770775
3369635310;4176548681;0.268080238
3369635310;4292094603;0.358251
3371598262;98978060;0.453521928

->

User,Events
3369635310,"[4292094603L, 4176548681L, ..., 2038842201L]"
...

"""

import pandas as pd
import difflib

const_ = "last"

def log3_(list_):
    f = open("res_"+const_+".csv", "w")
    f.write("User,Events\n")
    for x in list_:
        e = [long(i) for i in x['event']]
        f.write('%s,"%s"\n' % (x['user'], e))
    f.close()


def mk_(df):
    di = {user: [] for user in df["user"]}
    for i, row in df.iterrows():
        di[row["user"]].append([row["event"]] + [row["r"]])
    return di

def main():
    dataset = pd.read_csv('test_'+const_+'.csv', sep = ';')
    uu = mk_(dataset)

    al = []
    ozenka = 0.0

    for key, value in uu.iteritems():
        fns = []
        rrr = {} 
        rrr['user'] = key
        vv = 0
        for x in value:
            d = {}
            ev = x[0]
            sr = x[1]
            d['ev'] = ev
            d['sr'] = sr
            d['le'] = vv
            vv += 1
            fns.append(d)

        one_i = "".join([str(x['le']) for x in fns])
        fns = sorted(fns, key = lambda x: x['sr'], reverse=True)
        two_i = "".join([str(x['le']) for x in fns])

        ozenka += ( 1.0 - difflib.SequenceMatcher(None, one_i, two_i).ratio() )
 
        idx = [jj['ev'] for jj in fns]
        rrr['event'] = idx
        al.append(rrr)

    log3_(al)

    print "ozenka = %s\n" % ozenka

if __name__=="__main__":
    main()
