# A simple HTTP log analizator

## Intro

This is a very simple Python script for HTTP server logs analysis (so far tested with *Apache* and *LiteSpeed WebServer*).

## Usage

`python analizator.py logfile [keyword]`

If *keyword*, provided then the script ignores lines, which **don't** include it. I find it pretty useful, f.e. when you want to narrow your area of research.

Produces the following output:

`some_ip_1 => 2662 == 12.4608%  
some_ip_2 => 2475 == 11.5855%  
some_ip_3 => 1506 == 7.04957%  
some_ip_4 => 1157 == 5.41591%  
some_ip_5 => 356 == 1.66643%`

The pattern is: *IP address => number of occurences == % of total IP addresses*
