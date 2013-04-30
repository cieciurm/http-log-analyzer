# HTTP log analyzer

## Intro

This is a very simple Python script for HTTP server logs analysis.
So far tested with *Apache* and *LiteSpeed WebServer*.

## Usage

`$ python analizator.py [-i][-k keyword] logfile`

## Options

Availible options:
* `-i` show IP addresses instead of domain names,
* `-k keyword` search for a keyword in the logs.

## Output

Produces the following output:
> some_ip_1 => 2662 == 12.4608%  
> some_ip_2 => 2475 == 11.5855%  
> some_ip_3 => 1506 == 7.04957%  
> some_ip_4 => 1157 == 5.41591%  
> some_ip_5 => 356 == 1.66643%
> ...

The pattern is: *IP address => number of occurences == % of total IP addresses*

## TODO

Add a feature for generating .htaccess file banning IPs with number of requestes higher then provided treshold 
