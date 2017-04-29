# This is a script to apply a regular expression to parse the information from charm.py 
import re
import time
import sys
import string
import csv
import fileinput

filename = open("charm.txt", "r")
array = []
array2 = []
i = 0
pat  = re.compile(r"\w{3}\s(?P<date>\w{3}\s\d{1,2})\s(?P<time>\d\d:\d\d:\d\d)\s\+0000\s\d{4}[^2017]:\s(?P<message>\S.+)")
tap  = re.compile(r"\S.+\@(?P<contacts>\S+)\s\S.+")

for l in filename:
	p = pat.findall(l)
        if p:
                print p
		t= tap.findall(l)
		if t:
			print t
	else:
		exit

