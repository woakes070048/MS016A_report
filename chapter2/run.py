#!/usr/bin/env python
# -*- coding: utf-8 -*-

from httperfpy import Httperf
import csv
import os
import time
import argparse

# saturation:
# /usr/bin/httperf --hog --server balance1 --port 80 --uri="/perf.php?sleep=0.2" --num-conns=15000 --rate=2000 --num-call=1

def run_httperf(server, num_conns=None, rate=None, num_calls=None, sleep=None):
    if sleep:
        uri = '/perf.php?sleep={}'.format(sleep)
    else:
        uri = '/perf.php?sleep=0.2'
    perf = Httperf('hog', path='/usr/bin/httperf', server=server, port=80, uri=uri,
            num_conns=num_conns, rate=rate, num_calls=num_calls)
    perf.parser = True
    results = perf.run()

    print results

    return results

def write(filename, results):
    csv_data = []
    header = results.keys()
    if not os.path.isfile(filename):
        csv_data.append(header)

    with open(filename, 'a') as f:
        w = csv.DictWriter(f, results.keys)
        csv_data.append([results[x] for x in results])
        w.writer.writerows(csv_data)

def main(server):
    if server:
        servername = server
    else:
        servername = 'balance1'
    length = 60 # sec
    increase_by = 100
    rate = 100
    max_rate = 2000
    num_calls = 1
    times = 3
    sleep = 1

    filename = 'perf_%s_combined' % (servername)
    while rate <= max_rate:
        #filename = 'perf_%s_r%s' % (servername,rate)
        num_conns = rate * length

        for t in range(0,times):
            #result = run_httperf(servername, num_conns=1000, rate=25, num_calls=1)
            result = run_httperf(servername, num_conns=num_conns, rate=rate, num_calls=num_calls,sleep=sleep)
            write(filename, result)
            time.sleep(30)

        rate += increase_by

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Performance testing VIP")
    parser.add_argument('--server', metavar='server', default=None, help="Server to test")
    args = parser.parse_args()
    main(args.server)
