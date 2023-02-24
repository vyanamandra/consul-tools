#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Venu Yanamandra
# Created Date: Feb 24 2023
# Purpose     : Understand MaxQueryTime, DefaultQueryTime through KV query.
# ---------------------------------------------------------------------------

import sys
import requests
import argparse
from datetime import datetime


def dttm_this_get(url, key, index, consistent, wait, token):
    resp = ''
    status_code = 200
    get_url = '{}/v1/kv/{}?index={}'.format(url, key, index)
    
    if consistent:
        get_url = '{}&consistent='.format(get_url)
        
    if len(wait) > 0:
        get_url = '{}&wait={}'.format(get_url, wait)

    start = datetime.now()

    headers = None
    if len(token) > 0:
        headers = {'x-consul-token': token}

    try:
        r = requests.get(get_url, headers=headers, verify=False)
        status_code = r.status_code
        if r.ok:
            resp = str(r.json()[0])
        else:
            resp = 'Errored (does the key exist?)'

    except Exception as e:
        resp = 'Exception: <{}>'.format(e)

    end = datetime.now()

    return '{} | {} | {} | {} | {} | {}'.format(get_url, status_code, str(start), str(end), end - start, resp)


def main():
    parser = argparse.ArgumentParser(
        prog='{}'.format(sys.argv[0]), description='Understand BlockingQueries, MaxQueryTime, DefaultQueryTime through KV query.', epilog='Venu Yanamandra thanks you for trying. :)')
    parser.add_argument('-u', '--url', help='Consul HTTP Addr',
                        default='http://127.0.0.1:8500')
    key_required = parser.add_argument_group('Required arguments')
    key_required.add_argument('-k', '--key', required=True, help='Key to retrieve')
    parser.add_argument('-i', '--index', type=int, default=1)
    parser.add_argument('-c', '--consistent', type=bool, default=True)
    parser.add_argument('-w', '--wait', default='')
    parser.add_argument('-t', '--token', default='')

    args = parser.parse_args()

    r = dttm_this_get(args.url, args.key, args.index,
                      args.consistent, args.wait, args.token)

    print(r)


if __name__ == '__main__':
    main()
