# Autosign
## 目的：使用脚本，抢饿了么10元无门槛大红包<br>
### 步骤：<br>
1.安装依赖  pip install -r requirements.txt<br>

2.修改User.ini文件里的cookie和Agent的值，为用户本人的cookie和agent（可通过chares抓包获取）<br>

3.可运行下test.py文件，查看添加的cookie是否有效。如果运行结果“红包已被抢完，请在下个时间段再参与”代表没问题，如果“message":"未登录","name":"UNAUTHORIZED”代表
  cookie有问题<br>

4.运行脚本 python start.py  自动起定时任务，每天10点，14点，17点去抢（20点的脚本没写，因为大红包每天只能抢一次，一般来说前3个时间段至少会抢到一次）<br>

### 说明：<br>
1.本脚本也可以同时多人抢大红包<br>

使用详细介绍可点开链接：https://testerhome.com/topics/17223
