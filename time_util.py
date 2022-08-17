import common_util
import datetime

DT_NOW = datetime.datetime.now()
DT_NOW_TO_SHOW = str(DT_NOW.strftime('%Y-%m-%d %H:%M:%S'))

class Time:
  def __init__(self, hour, minute):
      self.hour = hour
      self.minute = minute
      
  def addTime(self,toAdd):
    sumMinute = self.hour*60
    sumMinute += self.minute
    sumMinute += toAdd.hour*60
    sumMinute += toAdd.minute
    res = Time(0,0)
    res.hour = int(sumMinute/60)
    res.minute = sumMinute%60
    return res
  
  def toStr(self,text="{}h{}m"):
    return text.format(self.hour, self.minute)

  def toHour(self):
    res = self.hour + int(self.minute/6)/10
    return res

def generateTime(str):#generate
    res = Time(0,0)
    hourS = minuteS = '0'
    if('h' in str):
      hourS = str.split('h')[0]
      if('m' in str):
        minuteS = str.split('h')[1].split('m')[0]
    else:
      minuteS = str.split('m')[0]
    errorMessage = '無効な引数です。:'+ str
    if(hourS.isdecimal()):
      res.hour = int(hourS)
    else:common_util.error(errorMessage)
    if(minuteS.isdecimal()):
      res.minute = int(minuteS)
    else:common_util.error(errorMessage)
    return res

def getSimpleDate():
  str(DT_NOW.month)+'/' + str(DT_NOW.day)

def getTimeToAdd(args,symbols):
  if('+' in symbols):
    idx = symbols.index('+')
    arg=args[idx][1:]
    toAdd = generateTime(arg)
  else:
    idx = symbols.index('-')
    arg=args[idx][1:]
    toAdd = generateTime(arg)
    toAdd.hour *= -1
    toAdd.minute *= -1
  return toAdd