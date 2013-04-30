import string, sys, operator, socket, getopt

# -b         - create .htaccess with banned IPs- TODO
# -k keyword - search for a given keyword
# -i         - use domain names

opts, arg = getopt.getopt(sys.argv[1:], 'bk:i')
arg = ''.join(arg)

keyword = ''
use_ip = False

if not arg:
	print >> sys.stderr, "\nError! Enter the logfile name!"
	exit()

print >> sys.stderr, "\nBrowsing file '%s'." % arg

if opts:
	print >> sys.stderr, "\nChosen options:"
for opt in opts:
	if opt[0] == '-b':
		print >> sys.stderr, "\t* banning"
	elif opt[0] == '-k':
		keyword = opt[1]
		print >> sys.stderr, "\t* searching for keyword '%s'" % keyword
	elif opt[0] == '-i':
		use_ip = True
		print >> sys.stderr, "\t* using IP adresses (not domain names)"

try:
	file = open(arg) # file with server logs
except IOError:
	print "\nError! Cannot open file '%s'" % arg
	exit()

ip = {} # dictionary for {ip adress/domain name: number of occurences}
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

if use_ip == True:
	rly_ip = {}
	for key in ip:
		# if -i option was given then try to convert domain into IP
		try:
			rly_ip_entry = socket.gethostbyname(key)
		except socket.error:
			rly_ip_entry = key
		rly_ip[rly_ip_entry] = ip[key]
	ip = rly_ip

# a sorted version of dictionary 'ip' - by values
sorted_ip = sorted(ip.iteritems(), key=operator.itemgetter(1), reverse=True)

# prints ip adress, number of occurences and % of total ip adresses 
for element in sorted_ip:
	percent = float(element[1]) / total_words * 100
	rounded_percent = round(percent, 2)
	print "%s => %d == %g%%" % (element[0], element[1], rounded_percent)
