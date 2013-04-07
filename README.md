# A simple HTTP log analizator

## Intro

This is a very simple script that analyzes logs from HTTP server (so far tested with Apache and LiteSpeed WebServer).

## Usage

`python analizator.py logfile [keyword]`

where keyword is a string that should be looked for in the log entries (found it pretty useful).

Produces the following output:

`some_ip_1 => 2662 == 12.4608%
some_ip_2 => 2475 == 11.5855%
some_ip_3 => 1506 == 7.04957%
some_ip_4 => 1157 == 5.41591%
some_ip_5 => 356 == 1.66643%`

IP address => number of occurences == % of total IP addresses 
