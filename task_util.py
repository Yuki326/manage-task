import sys
import path
import common_util
import time_util

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
    res = time_util.Time(0,0)
    hourS = minuteS = '0'
    if('h' in self.time):
      hourS = self.time.split('h')[0]
      if('m' in self.time):
        minuteS = self.time.split('h')[1].split('m')[0]
    else:
      minuteS = self.time.split('m')[0]
    errorMessage = '無効な引数です。:'+self.time
    if(hourS.isdecimal()):
      res.hour = int(hourS)
    else:common_util.error(errorMessage)
    if(minuteS.isdecimal()):
      res.minute = int(minuteS)
    else:common_util.error(errorMessage)
    return res

  def toStr(self):
    text = "{} {} {} {} {} {}\n"
    return text.format(self.id, self.title,self.start,self.end,self.time,self.state)

def getText(tasks):
  text = ''
  for i in range(len(tasks)):
    text += tasks[i].toStr()
  return text

def getTasks():
  f = open(path.Path+'taskList.txt', 'r+',encoding="utf-8")
  areas = f.read().split()
  tasks = []
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
          tasks.append(tmp)
  f.close()
  return tasks

def updateTasks(tasks):
  common_util.quick_sort(tasks,cmpState)
  text = getText(tasks)
  if(type(text)!=str):sys.exit()
  f = open(path.Path+'taskList.txt', 'w',encoding="utf-8")#ファイルの中身が消えるので注意
  f.write(text)
  f.close()

def getTaskById(tasks,id):
  for i in range(len(tasks)):
    if tasks[i].id == id:
      return i
  return -1

def cmpState(s1,s2):
  lst = ['progress','todo','wait','done','resolved']
  n1 = n2 = 100
  if(s1.state in lst):
    n1 = lst.index(s1.state)
  if(s2.state in lst):
    n2 = lst.index(s2.state)
  if(n1<n2):
    return 1
  elif(n1>n2):
    return -1
  else:
    return 0
  
