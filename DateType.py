#! python3
# DateType.py. - This script will search for filenames with American date order
# and format the to european date order.

import shutil, os, re

# We create a regex that matches files with the American date format.

datePattern = re.compile(r'''
	^(.*?) 		    #all text before the date
	((0|1)?\d)-	    #month(one or two digits)
	((0|1|2|3)?\d)- #day(one or two digits)
	((19|20)\d\d)   #year(Four digits for the year)
	(.*?)$			#all the text after the date
	''', re.VERBOSE)

# Loop over the files in the working directory.
for filename in os.listdir('.'):
	mo = datePattern.search(filename)
# Skip files without a date
	if mo == None:
		continue
		
# Get the different parts of the filenames
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)
# Form a European-Style filename 
	euroFileName = beforePart + dayPart + monthPart + yearPart + afterPart
# Get the full, absolute file paths
	abspathwdir = os.path.abspath('.')
	filename = os.path.join(abspathwdir, filename)
	euroFileName = os.path.join(abspathwdir, euroFileName)

# Rename the files
	print('Renaming "%s" to "%s"...'%(filename,euroFileName))
	shutil.move(filename, euroFileName)