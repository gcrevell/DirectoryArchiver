#!/usr/bin/env python

import sys 			# CL Args
import subprocess	# Needed to run shell commands
import urllib		# Needed to decode name if url encoded
import time

def downloadFile(url, dest='/', name=None, retries=3, maxTime = 60):
	'''Download a file and stream it to the destination on ACD.'''
	
	if name is None:
		# Parse name from url
		name = url[url.rfind('/') + 1:]
		if '?' in name:
			name = name[:name.find('?')]
	
		name = urllib.unquote(name).decode('utf8')
		
	if name[0] is '-':
		# acd_cli needs a double dash in front of arguments starting with a dash
		name = '-- ' + name
	
	t = 2	# Wait time between requests

	# While we have retries...
	while retries > 0:
		try:
			# Run shell command. This is blocking.
			ret = subprocess.check_call('curl -s "{}" | ./acd/acd_cli_custom.py -i none stream --overwrite --quiet "{}" "{}"'.format(url, name, dest), shell = True )
			break
		except KeyboardInterrupt:
			# If we get a keyboard interrupt, raise it to exit
			raise
		except:
			# Otherwise, decrement tries
			retries -= 1
			if retries == 0:
				# If 0 tries, skip waiting
				break

			# Wait, then double time. This allows for quick backoff for too many requests
			time.sleep(t)
			t = max(2 * t, maxTime)

def main():
	'''The main program. Parses arguments in format [URL] [Dest] {Name}'''
	
	if len(sys.argv) < 3 or len(sys.argv) > 4:
		# Wrong number of arguments.
		print 'Proper use: ' + sys.argv[0] + ' [URL] [Dest] {Name}'

	downloadFile(sys.argv[1], dest = sys.argv[2], name = sys.argv[3] if 3 < len(sys.argv) else None)


if __name__ == '__main__':
	main()
