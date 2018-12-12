#!/usr/bin/python
#-*- coding: UTF-8 -*-
import threading,datetime,time
from apscheduler .schedulers.blocking import BlockingScheduler
from ElemBigHongbao import gethongbao

def hongbao_default():
    return gethongbao("default")
scheduler = BlockingScheduler()
#default用户
scheduler.add_job(hongbao_default,'cron',hour=9,minute=59,second=59)
scheduler.add_job(hongbao_default,'cron',hour=13,minute=59,second=59)
scheduler.add_job(hongbao_default,'cron',hour=16,minute=59,second=59)


print("开始执行"+datetime.datetime.now().strftime('%H:%M:%S.%f'))
scheduler.start()