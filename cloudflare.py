#!./env/bin/python3

import sys
import argparse
import os
import json
import datetime
import requests
from subprocess import call
from collections import Counter
server = "https://api.cloudflare.com/client/v4/"


def zoneSearch(zoneName):
    result = False
    sess = requests.Session()
    # sess.auth = (user, passwd)
    sess.headers.update({"X-Auth-Email": args.user,
                         "X-Auth-Key": args.key, "Content-Type": "application/json"})

    resp = sess.get(server+"zones")
    # print(resp.json())
    for project in resp.json()['result']:
        if args.project in project['name']:
            print('Found {} : {}'.format(
                project['name'], project['id']))
            id = project['id']
            result = True

    if result:
        return id
    else:
        print('Project {} Not Found'.format(zoneName))
        exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cloudflare cli')
    parser.add_argument('action', help='ACTION what to do', choices=[
                        'clear-cache', ], default='clear-cache')
    parser.add_argument(
        '-p', '--project', default="none")
    parser.add_argument(
        '-u', '--user', default=os.environ.get('CLOUDFLARE_EMAIL', None))
    parser.add_argument(
        '-k', '--key', default=os.environ.get('CLOUDFLARE_KEY', None))

    args = parser.parse_args()

if not args.user or not args.key:
    print('Please set the environment values CLOUDFLARE_EMAIL and CLOUDFLARE_KEY or set user and key as defined below')
    exit(parser.print_usage())

if 'clear-cache' in args.action:

    id = zoneSearch(args.project)
    # zones/023e105f4ecef8ad9ca31a8372d0c353/purge_cache
    sess = requests.Session()
    # sess.auth = (user, passwd)
    sess.headers.update({"X-Auth-Email": args.user,
                         "X-Auth-Key": args.key, "Content-Type": "application/json"})
    data_post = {}
    data_post["purge_everything"] = True
    resp = sess.post(server+"zones/"+id+"/purge_cache",
                     data=json.dumps(data_post))

    if resp.status_code == 200 and resp.json()['success']:
        print('Cache cleared for {}'.format(args.project))
        exit(0)
    else:
        print('Error: {}'.format(resp.json()))
        exit(1)
