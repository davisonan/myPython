#!/usr/bin/python -tt
import sys
import os
from datetime import date
from datetime import timedelta

#-----------------------------------
# Define a main() function 
def main():
    if len(sys.argv) < 3:
        print '\tWrong input arguments. Use ./runPigDates.py filename dateFrom [dateTo] [additional arguments] \r\n\tExample: ./runPigDates.py theScript.pig 20120820 20120910 "-p bucket=DFD5"'
    else:
        pigfile = sys.argv[1]
        dateFr = sys.argv[2]

    #dateTo:
    if len(sys.argv) > 3:
        dateTo = sys.argv[3]
    else:
        dateTo = dateFr

    #params:
    if len(sys.argv) > 4:
        params = ' ' + sys.argv[4] + ' '
    else:
        params = ' '

    filename = pigfile[:-4]
    dateFr = date(int(dateFr[:4]), int(dateFr[4:6]), int(dateFr[6:]))
    dateTo = date(int(dateTo[:4]), int(dateTo[4:6]), int(dateTo[6:]))
    delDir = raw_input("Delete hdfs " + filename + " directory (blank/default means NO)? [y/n] ")
    tailQ = raw_input("Tail nohup file (blank means YES)? [y/n] ")

    while dateFr <= dateTo:
        dates = dateFr.strftime("%Y%m%d")

        # Delete old directories
        if delDir == '1' or delDir == 'y' or delDir == 'yes':
            delDirStr = 'hadoop fs -rm -r -skipTrash ' + filename + '/' + dates
            print delDirStr
            os.system(delDirStr);

        # Run pig
        runStr = 'nohup pig -latest -Dmapred.job.queue.name=adhoc -p dates=' + dates + ' -p outputDir = ' + filename + '/' + dates + params + filename + '.pig > nohup_' + filename + '_' + dates + '.out &'
        print runStr
        os.system(runStr);
        dateFr = dateFr + timedelta(days=1)

    #  Tail nohup file
    if tailQ == 'y' or tailQ == '':
        tailStr = 'tail -f nohup_' + filename + '_' + dates + '.out'
        os.system(tailStr);

#-----------------------------------
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
