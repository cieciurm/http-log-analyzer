import string, sys, operator

argc = len(sys.argv)

if argc == 1:
	print "Enter the logfile name"
	exit()

file = open(sys.argv[1]) # file with server logs

if argc == 2:
	word_to_look_for = '' # if only 1 argument given
else:
	word_to_look_for = sys.argv[2] # if 2 arguments given - 
# a word to look for in logs

ip = {} # dictionary for {ip adress: number of occurences}
total_words = 0.0 # total number of ips in the dictionary

for line in file.readlines():
	if word_to_look_for in line:
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
	print "%s => %d == %g%%" % (element[0], element[1], float(element[1])/total_words*100)
# prints ip adress, number of occurences and % of total ip adresses 
