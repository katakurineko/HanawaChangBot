# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:31:19 2019

@author: nekot
"""

import slack

SLACK_API_TOKEN = ""

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'こんにちは' in data.get('text', []) and data.get('user',False):
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"こんにちは、<@{user}>!",
            thread_ts=thread_ts
        )

rtm_client = slack.RTMClient(token=SLACK_API_TOKEN)

try:
    rtm_client.start()
except KeyboardInterrupt:
    rtm_client.stop()