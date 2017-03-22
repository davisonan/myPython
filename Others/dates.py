#!/usr/bin/python -tt

from datetime import date
from datetime import timedelta

def main():
	file = open("datefile", 'w')
	dateFr = date(2014, 1, 1)
	dateTo = date(2014, 9, 12)
	while dateFr <= dateTo:
		dates = dateFr.strftime("%Y%m%d")
		file.write(dates+'\n')
		dateFr = dateFr + timedelta(days=1)
if __name__ == '__main__':
	main()