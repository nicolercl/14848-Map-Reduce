import sys

cur_date = None
cur_tmp = 0
date = None

with open("results.txt", 'w+') as f:
    for i, line in enumerate(sys.stdin):
        line = line.strip()
        date, tmp = line.split('\t', 1)
        if date == "None":
            print(i)
        try:
            tmp = int(tmp)
        except ValueError:
            continue
        if date == cur_date:
            if cur_tmp < tmp:
                cur_tmp = tmp
        else:
            if cur_date:
                f.write("%s\t%d\n" % (cur_date, cur_tmp))
            cur_date = date
            cur_tmp = tmp

    if date == cur_date:
        f.write("%s\t%d\n" % (cur_date, cur_tmp))
