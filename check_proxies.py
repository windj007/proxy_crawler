#!/usr/bin/env python

import sys, os, argparse, requests
import multiprocessing as mp


aparser = argparse.ArgumentParser(sys.argv[0])
aparser.add_argument('in_file', type = str, help='source file containing list of proxies')
aparser.add_argument('out_file', type = str, help='file to write filtered proxies to')
aparser.add_argument('-p', metavar = 'proc_cnt', type = int, default = 20, help='amount of processes to use for proxy checking')
aparser.add_argument('-t', metavar = 'timeout', type = float, default = 10.0, help='connection timeout (in seconds)')
args = aparser.parse_args()


if args.in_file == "-":
    infile = sys.stdin
elif os.path.exists(args.in_file):
    infile = open(args.in_file, 'r')
else:
    print >> sys.stderr, "Input file '%s' does not exist" % args.in_file
    exit(1)

if args.out_file == "-":
    outfile = sys.stdout
else:
    outfile = open(args.out_file, 'w')


def check_proxy(address):
    try:
        resp = requests.head('http://www.amazon.com', proxies = { 'http': address }, timeout = args.t)
        return address if resp.status_code < 400 else None
    except Exception:
        return None

checkpool = mp.Pool(processes = args.p)
print >> outfile, "\n".join([addr for addr in checkpool.map(check_proxy, map(str.strip, infile)) if addr])
