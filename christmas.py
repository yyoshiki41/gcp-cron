# coding:utf-8

import os
import json
import requests

URL = "http://www.tbs.co.jp/kanran/"
req = requests.get(URL)
message = ""

if req.status_code == 200:
    req.encoding = req.apparent_encoding
    r = req.text.encode('utf-8')
    for line in r.splitlines():
        if line.find("クリスマスの約束") >= 0:
            message += line
        if line.find("小田和正") >= 0:
            message += line
        if line.find("バナナマン") >= 0:
            message += line

if len(message) > 0:
    webhooksURL = os.environ["SLACK_URL"]
    payload_dic = {
        "channel": '@yyoshiki41',
        "username": 'クリスマスの約束',
        "icon_emoji": ':christmas_tree:',
        "text": "```\n"+message+"\n```",
    }
    requests.post(webhooksURL, data=json.dumps(payload_dic))
