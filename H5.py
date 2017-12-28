from selenium import webdriver
import csv
from itertools import islice
from urllib import parse



str1=r'https://coupon.m.jd.com/union?mtm_source=kepler-open&mtm_subsource='#协议头#
str2=r'&mopenbp7='
str3=r'&returl='

csv_data = csv.reader(open("sourceurl.csv"))
result = []
errorFile = open("result.csv", 'w',newline ='')
writeCSV = csv.writer(errorFile)

for row in islice(csv_data, 1, None):
    tstr=row[1]
    print(tstr)
    tstr2=row[2]
    tstr3=row[3]
    parse.quote_plus
    par=str1+tstr3+str2+tstr2+str3+parse.quote_plus(row[1])
    row[4]=par
    writeCSV.writerow(row)

