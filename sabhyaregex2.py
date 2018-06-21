import csv
import re

with open('test.csv',newline='') as fh:
    with open('testout.csv','a', newline='') as fo:
        writer=csv.writer(fo)
        reader=csv.reader(fh)
        for row in reader:
            for index in range(len(row)):
                row[index]=re.sub(r'e(.)e', 'a\g<1>a', row[index])
            writer.writerow(row)
        print("Work done")

