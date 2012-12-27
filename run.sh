#!/bin/bash

[ -e proxy.log ] && rm proxy.log
scrapy crawl Proxy
