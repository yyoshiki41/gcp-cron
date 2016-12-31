# coding:utf-8

import os
import logging
import json
import urllib2

url = "http://www.tbs.co.jp/kanran/"

try:
    req = urllib2.urlopen(url)

    message = ""
    #req.encoding = req.apparent_encoding
    r = req.read()
    for line in r.splitlines():
        if line.find("クリスマスの約束") >= 0:
            message += line
        if line.find("小田和正") >= 0:
            message += line
    if len(message) > 0:
        webhook = os.environ["SLACK_URL"]
        payload = {
            "channel": '@yyoshiki41',
            "username": 'クリスマスの約束',
            "icon_emoji": ':christmas_tree:',
            "text": "```\n"+message+"\n```",
        }
        request = urllib2.Request(webhook, json.dumps(payload), {'Content-Type': 'application/json'})
        urllib2.urlopen(request)

except urllib2.URLError:
    logging.exception('Caught exception fetching url')

