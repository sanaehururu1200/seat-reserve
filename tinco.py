#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import signal
import sys
import random
from slackclient import SlackClient

def post(sc):
    print sc.api_call(
            "chat.postMessage", channel="#なぼへXXXする", text="<@XXX> かわいいよなぼちゃん♡",
            username='りこたそ', icon_emoji=':なぼたん:'
            )

    def handler(signum, frame):
        print 'Signal handler called with signal',signum
    GPIO.cleanup()
    sys.exit(0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN)
before = 0
token = "XXX"
sc = SlackClient(token)

now = GPIO.input(9)
if before == 0 and now == 1:
      aikatsu = ['軍艦島座席番号1','軍艦島座席番号2','軍艦島座席番号3','軍艦島座席番号4','軍艦島座席番号5','軍艦島座席番号6','屋久島座席番号1','屋久島座席番号2','屋久島座席番号3','屋久島座席番号4','屋久島座席番号5','屋久島座席番号6','小豆島座席番号1','小豆島座席番号2','小豆島座席番号3','小豆島座席番号4','小豆島座席番号5','小豆島座席番号6','種子島座席番号1','種子島座席番号2','種子島座席番号3','種子島座席番号4','種子島座席番号5','種子島座席番号6','佐渡島座席番号1','佐渡島座席番号2','佐渡島座席番号3','佐渡島座席番号4','佐渡島座席番号5','佐渡島座席番号6']
      print(random.choice(aikatsu))
      time.sleep(0.1)
before = now
