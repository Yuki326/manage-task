import sys

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
  
  def toStr(self):
    text = "{}h{}m"
    return text.format(self.hour, self.minute)

  def toHour(self):
    res = self.hour + int(self.minute/6)/10
    return res

class Task:
  
   # コンストラクタ
  def __init__(self, id, title,start,end,time, state):
    self.id = id
    self.title = title
    self.start = start
    self.end = end
    self.time = time
    self.state = state

  def getTime(self):
    res = Time(0,0)
    if('h' in self.time):
      res.hour = int(self.time.split('h')[0])
      if('m' in self.time):
        res.minute = int(self.time.split('h')[1].split('m')[0])
    # else:
    #   res.minute = int(self.time.split('m')[0])
    return res

  def toStr(self):
    text = "{} {} {} {} {} {}\n"
    return text.format(self.id, self.title,self.start,self.end,self.time,self.state)

def getText(data):
  text = ''
  for i in range(len(data)):
    text += data[i].toStr()
  return text

def getData():
  f = open('Record/test.txt', 'r+',encoding="utf-8")
  areas = f.read().split()
  data = []
  tmp={}
  for i in range(len(areas)):
      if(i%6==0):
          tmp = Task('','','','','','')
          tmp.id=areas[i]
      if(i%6==1):
          tmp.title=areas[i]
      if(i%6==2):
          tmp.start=areas[i]
      if(i%6==3):
          tmp.end=areas[i]
      if(i%6==4):
          tmp.time=areas[i]
      if(i%6==5):
          tmp.state = areas[i]
          data.append(tmp)
  f.close()
  return data

def updateData(data):
  text = getText(data)
  if(type(text)!=str):sys.exit()
  f = open('Record/test.txt', 'w',encoding="utf-8")#ファイルの中身が消えるので注意
  f.write(text)
  f.close()

def getTaskById(data,id):
  for i in range(len(data)):
    if data[i].id == id:
      return i
  return -1

def getTime(str):
    res = Time(0,0)
    if('h' in str):
      res.hour = int(str.split('h')[0])
      if('m' in str):
        res.minute = int(str.split('h')[1].split('m')[0])
    else:
      res.minute = int(str.split('m')[0])
    return res