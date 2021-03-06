# pdfparser.py

from PyPDF2 import PdfFileReader
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

pdfFileObj = open('Resume (Xu Tian).pdf', 'rb')
resume = PdfFileReader(pdfFileObj)

# print the title of document1.pdf
print("title = %s" % (resume.getDocumentInfo().title))

# add page 1 from input1 to output document, unchanged
contents = resume.getPage(0).extractText()

# Close the pdf file at the end.
pdfFileObj.close()

"""
The script is used to parse PDF and DOCX files predominantly resumes and extract all the relevant information from it.
The extracted information is stored on to a Django model, this can be replaced to suite your needs.
"""
__author__ = "ssharad"
__license__ = "GPL v.3.0"
# -*- coding: utf-8 -*-
import pyPdf
import docx
import string



tokens = word_tokenize(resume)
punctuations = ['(',')',';',':','[',']',',']
stop_words = stopwords.words('english')
#storing the cleaned resume
filtered = [w for w in tokens if not w in stop_words and  not w in string.punctuation]
print "removing the stop words....\nCleaning the resumes....\nExtracting Text ......."
print filtered
#get the name from the resume
name  = str(filtered[0])+' ' +str(filtered[1])
print "Name : " + name

#using regular expressions we extract phone numbers and mail ids
import re
#get contact info - from resume
#email
email = ""
match_mail = re.search(r'[\w\.-]+@[\w\.-]+', resume)
#handling the cases when mobile number is not given
if(match_mail != None):
    email = match_mail.group(0)
print "Email : " + email

#mobile number
mobile = ""
match_mobile = re.search(r'((?:\(?\+91\)?)?\d{9})',resume)
#handling the cases when mobile number is not given
if(match_mobile != None):
    mobile = match_mobile.group(0)
print "Mobile : " +  mobile

parsed_resume = ' '.join(filtered)
print "Parsed Resume in plain Text : ", parsed_resume
r = str(parsed_resume)

#shingles - for eeach parsed resume
shingle = []
# form n-grams - basically the singles for LSH
from nltk.util import ngrams
#form the shingles of the filtered resume - the length of each shingle is 10
make_shingle = ngrams(filtered,10)
#print the shingles
for s in make_shingle:
    shingle.append(s)  

print "Shingles for the resume : ",shingle
#save the name and contact details in separate fields - the parsed resume in anohter field
# the parsed information is stored in a database (Django Model)
import django
#configure the Django envronment to the location of your app
import os
import sys
sys.path.append('/home/sharad/resumes/')
os.environ['DJANGO_SETTINGS_MODULE']='resumes.settings'
django.setup()
#os.environ.setdefault(“DJANGO_SETTINGS_MODULE”, “resumes.settings”)
from django.conf import settings
#Edit the django model
from view_db.models import parsed_resume
#add the new entries to the table
r = parsed_resume(name = name,email = email, mobile = mobile, parsed_resume = r, shingles = shingle)
#commit the changes
r.save()
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help