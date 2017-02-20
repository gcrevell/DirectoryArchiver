#!/usr/bin/env python

import sys 			# CL Args
import re			# Regex. Needed for URL validation
import subprocess	# Needed to run shell commands

def downloadFile(url, dest, name=None):
	if name is None:
    	# Parse name from url
    	name = url[url.rfind('/'):]
       
    # Run shell command. This is blocking. 
	subprocess.check_output('curl -s -S "{}" | ./acd/acd_cli -i none stream --overwrite --quiet "{}" "{}"'.format(url, name, dest), shell = True )

def main():
	'''The main program. Parses arguments in format [URL] [Dest] {Name}'''

	if sys.argc < 3 || sys.argc > 4:
    	# Wrong number of arguments.
        print 'Proper use: ' + sys.argv[0] + ' [URL] [Dest] {Name}'




if __name__ == '__main__':
	main()
