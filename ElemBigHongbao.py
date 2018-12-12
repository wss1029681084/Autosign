#!/usr/bin/python
#-*- coding: UTF-8 -*-
import requests
import logging
import threading,datetime,time
import Tools,os

def gethongbao(user):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=os.path.dirname(__file__)+'/elem.log',
                        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    logging.info("start time" + datetime.datetime.now().strftime('%H:%M:%S.%f'))
    def hongbao():
        Agent =Tools.GetAgent(user)
        cookie2 = requests.utils.cookiejar_from_dict(Tools.GetCookie(user))
        headers = {'User-agent': Agent}
        user_id=Tools.GetUserid(user)
        url2 = "https://h5.ele.me/restapi/member/v1/users/"+user_id+"/sign_in/limit/hongbao"
        data = {"user_id": user_id, "latitude": 31.250972747802734, "longitude": 121.51678466796875}
        n = 0


        time.sleep(0.8)
        while n < 10:
            n = n + 1
            res2 = requests.post(url2, data, cookies=cookie2, headers=headers) \
                .content.decode('utf-8')
            logging.info(datetime.datetime.now().strftime('%H:%M:%S.%f')+res2)

    t = threading.Thread(target=hongbao, name='LoopThread')
    t.start()
    t.join()





