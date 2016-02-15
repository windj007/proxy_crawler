#!/bin/bash

crawl_result_file='last_proxies.lst'

[ -e result_file ] && rm $crawl_result_file
[ -e proxy.log ] && rm proxy.log

scrapy crawl Proxy -s PROXY_RESULTS_FILE=$crawl_result_file
sort -n -u $crawl_result_file -o $crawl_result_file
./check_proxies.py -p 500 $crawl_result_file "proxies_checked.lst"

