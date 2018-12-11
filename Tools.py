import configparser
config = configparser.ConfigParser()
config.read("User.ini",encoding='UTF8')
#StrTodict能转换str为dict格式
def StrTodict(str):
  s1 = str.split(";")
  dict = {}
  for s in s1:

    s2=s.split("=")
    dict[s2[0]]=s2[1]
  return dict

def GetCookie(user):
  cookie=config.get(user,"cookie")
  return StrTodict(cookie)

def GetAgent(user):
  return config.get(user,"Agent")

