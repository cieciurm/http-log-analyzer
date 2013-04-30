import string, sys, operator, getopt

# b - create .htaccess with banned IPs- TODO
# k - search for a given keyword

opts, arg = getopt.getopt(sys.argv[1:], 'bk:')
arg = ''.join(arg)

if not arg:
	print "\nError! Enter the logfile name!"
	exit()

keyword = ''

print "\nBrowsing file '%s'." % arg

if opts:
	print "\nChosen options:"
for opt in opts:
	if opt[0] == '-b':
		print "\t* banning"
	elif opt[0] == '-k':
		keyword = opt[1]
		print "\t* searching for keyword '%s'" % keyword

try:
	file = open(arg) # file with server logs
except IOError:
	print "\nError! Cannot open file '%s'" % arg
	exit()

print "----------------------------------------------------"

ip = {} # dictionary for {ip adress: number of occurences}
total_words = 0.0 # total number of ips in the dictionary

for line in file.readlines():
	if keyword in line:
		split_array = string.split(line)
		split_ip = split_array[0] # ip adress in [0]
		if split_ip in ip: # if already in the dict
			ip[split_ip] +=1
		else: # not yet in dict, add
			ip[split_ip] = 1
		total_words += 1

sorted_ip = sorted(ip.iteritems(), key=operator.itemgetter(1), reverse=True)
# a sorted version of dictionary 'ip' - by values

for element in sorted_ip:
	percent = float(element[1])/total_words*100
	rounded_percent = round(percent, 2)
	print "%s => %d == %g%%" % (element[0], element[1], rounded_percent)
# prints ip adress, number of occurences and % of total ip adresses 
