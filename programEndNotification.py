# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:23:48 2019

@author: ryunosuke.kotaki

https://api.slack.com/apps/ARAU94BSP

https://github.com/slackapi/python-slackclient/tree/bb49585f02e9a144dde9742207bf2b469a5475b7#basic-usage-of-the-web-client

Tips

# RuntimeErrorについて

なぜか、tornadoパッケージのバージョンによってはRuntimeErrorになるようです。
どうやらtornadoのバージョンを4.5.3にすればなおるらしい…。
https://github.com/jupyter/notebook/issues/3397#issuecomment-383452306

"""

import slack

client = slack.WebClient("")

response = client.chat_postMessage(
    channel='#bot実験場',
    text="<@UN1LRG57U> プログラムが終了したよ!")

print(response)