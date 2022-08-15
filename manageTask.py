from cgitb import reset
from pydoc import describe
from timeit import timeit
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

class Task:
  
   # コンストラクタ
  def __init__(self, id, description, time, state):
    self.id = id
    self.description = description
    self.time = time
    self.state = state

  def getTime(self):
    res = Time(0,0)
    #time = {'hour':0,'minute':0}#todo インターフェース
    print(self.time)
    if('h' in self.time):
      res.hour = int(self.time.split('h')[0])
      if('m' in self.time):
        print(self.time.split('h')[1].split('m')[0])
        res.minute = int(self.time.split('h')[1].split('m')[0])
    # else:
    #   res.minute = int(self.time.split('m')[0])
    return res

  def toStr(self):
    text = "{} {} {} {}\n"
    return text.format(self.id, self.description,self.time,self.state)

def getText(data):
  text = ''
  for i in range(len(data)):
    text += data[i].toStr()
  return text

f = open('test.txt', 'r+',encoding="utf-8")
areas = f.read().split()
data = []
tmp={}
for i in range(len(areas)):
    if(i%4==0):
        tmp = Task('','','','')
        tmp.id=areas[i]
    if(i%4==1):
        tmp.description=areas[i]
    if(i%4==2):
        tmp.time=areas[i]
    if(i%4==3):
        tmp.state = areas[i]
        data.append(tmp)
f.close()
t1 = data[0].getTime()
t2 = data[1].getTime()
t = t1.addTime(t2)
print(t.hour,t.minute)
data[0].time= t.toStr()

f = open('test.txt', 'w',encoding="utf-8")
f.write(getText(data))
f.close()
#print(data)
#print(getTime(data[1]['time']))
