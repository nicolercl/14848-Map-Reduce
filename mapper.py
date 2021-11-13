import sys

valid_qualities = [0, 1, 4, 5, 9]
for line in sys.stdin:
    line = line.strip()
    date = line[15:23]
    temp = int(line[87:92])
    quality = int(line[92])
    if temp != 9999 and quality in valid_qualities:
        print('%s\t%d' % (date, temp))