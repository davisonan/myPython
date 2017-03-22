#!/usr/bin/python -tt
import sys
import os
import datetime
import calendar
from datetime import date
from datetime import timedelta

#-----------------------------------
# Define a add_months() function 
def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)

#-----------------------------------
# Define a main() function 
def main():
    if len(sys.argv) < 3:
        print '\tWrong input arguments. Use ./runPigDates.py filename dateFr [additional arguments] \r\n\tExample: ./runPigSUR.py theScript.pig 20130301 "-p bucket=DFD5"'
    else:
        pigfile = sys.argv[1]
        dateFr = sys.argv[2]

   #params:
    if len(sys.argv) > 3:
        params = ' ' + sys.argv[3] + ' '
    else:
        params = ' '

    filename = pigfile[:-4]
    delDir = raw_input("Delete hdfs " + filename + " directory (blank/default means NO)? [y/n] ")
    tailQ = raw_input("Tail nohup file (blank means YES)? [y/n] ")

    # The initial dates of the sampling periods    
    dateFr = date(int(dateFr[:4]), int(dateFr[4:6]), int(dateFr[6:]))
    datesFr = dateFr.strftime("%Y%m%d")
    dateFr_w0 = dateFr
    dateFr_w1 = dateFr + timedelta(days=14)
    dateFr_m1 = add_months(dateFr_w0, 1)
    dateFr_m3 = add_months(dateFr_w0, 3)
    dateFr_m6 = add_months(dateFr_w0, 6)

    # The initial dates of the sampling periods in string formats
    dates_w0 = dateFr_w0.strftime("%Y%m%d")
    dates_w1 = dateFr_w1.strftime("%Y%m%d")
    dates_m1 = dateFr_m1.strftime("%Y%m%d")
    dates_m3 = dateFr_m3.strftime("%Y%m%d")
    dates_m6 = dateFr_m6.strftime("%Y%m%d")

    # The dates of the sampling periods in string formats
    for t in range(6):
        dateFr_w0 = dateFr_w0 + timedelta(days=1)
        dateFr_w1 = dateFr_w1 + timedelta(days=1)
        dateFr_m1 = dateFr_m1 + timedelta(days=1)
        dateFr_m3 = dateFr_m3 + timedelta(days=1)
        dateFr_m6 = dateFr_m6 + timedelta(days=1)
        dates_w0 = dates_w0 + ',' + dateFr_w0.strftime("%Y%m%d")
        dates_w1 = dates_w1 + ',' + dateFr_w1.strftime("%Y%m%d")
        dates_m1 = dates_m1 + ',' + dateFr_m1.strftime("%Y%m%d")
        dates_m3 = dates_m3 + ',' + dateFr_m3.strftime("%Y%m%d")
        dates_m6 = dates_m6 + ',' + dateFr_m6.strftime("%Y%m%d")

    # The current date
    day_cur = datetime.date.today();

    # Compare the periods with the current date to invoke/run different pig scripts.
    if day_cur > dateFr_m6:
        params_all = ' -p outputDir=SUR/' + datesFr + ' -p dates_w0=' + dates_w0 + ' -p dates_w1=' + dates_w1 + ' -p dates_m1=' + dates_m1 + ' -p dates_m3=' + dates_m3 + ' -p dates_m6=' + dates_m6
        runStr = 'nohup pig -latest -Dmapred.job.queue.name=adhoc' + params_all + params + filename + '_all.pig > nohup_' + filename + '_' + datesFr + '.out &'
    if (day_cur > dateFr_m3) and (day_cur < dateFr_m6):
        params_m3 = ' -p outputDir=SUR/' + datesFr + ' -p dates_w0=' + dates_w0 + ' -p dates_w1=' + dates_w1 + ' -p dates_m1=' + dates_m1 + ' -p dates_m3=' + dates_m3
        runStr = 'nohup pig -latest -Dmapred.job.queue.name=adhoc' + params_m3 + params + filename + '_m3.pig > nohup_' + filename + '_' + datesFr + '.out &'
    if (day_cur > dateFr_m1) and (day_cur < dateFr_m3):
        params_m1 = ' -p outputDir=SUR/' + datesFr + ' -p dates_w0=' + dates_w0 + ' -p dates_w1=' + dates_w1 + ' -p dates_m1=' + dates_m1
        runStr = 'nohup pig -latest -Dmapred.job.queue.name=adhoc' + params_m1 + params + filename + '_m1.pig > nohup_' + filename + '_' + datesFr + '.out &'
    if (day_cur > dateFr_w1) and (day_cur < dateFr_m1):
        params_w1 = ' -p outputDir=SUR/' + datesFr + ' -p dates_w0=' + dates_w0 + ' -p dates_w1=' + dates_w1
        runStr = 'nohup pig -latest -Dmapred.job.queue.name=adhoc' + params_w1 + params + filename + '_w1.pig > nohup_' + filename + '_' + datesFr + '.out &'

    print runStr
    os.system(runStr)

    if delDir == '1' or delDir == 'y' or delDir == 'yes':
        delDirStr = 'hadoop fs -rm -r -skipTrash ' + filename + '/' + datesFr
        print delDirStr
        os.system(delDirStr);

    #  Tail nohup file
    if tailQ == 'y' or tailQ == '':
        tailStr = 'tail -f nohup_' + filename + '_' + datesFr + '.out'
        os.system(tailStr);

#-----------------------------------
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()