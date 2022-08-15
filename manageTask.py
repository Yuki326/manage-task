import sys
class Time:
  def __init__(self, hour, minute):
      self.hour = hour
      self.minute = minute
      
  def addTime(self,toAdd,isPlus):
    sumMinute = self.hour*60
    sumMinute += self.minute
    if(isPlus):#todo 正負判定を早めにする
      sumMinute += toAdd.hour*60
      sumMinute += toAdd.minute
    else:
      sumMinute -= toAdd.hour*60
      sumMinute -= toAdd.minute
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
    if('h' in self.time):
      res.hour = int(self.time.split('h')[0])
      if('m' in self.time):
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

def getData():
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
  return data

def updateData(data):
  text = getText(data)
  if(type(text)!=str):sys.exit()
  f = open('test.txt', 'w',encoding="utf-8")#ファイルの中身が消えるので注意
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

args = sys.argv
if(len(args)==1):
  print('コマンドライン引数を入力してください')
  sys.exit()

data = getData()
idx = getTaskById(data,args[1])
if(idx == -1):
  data.append(Task(args[1],'#','0m','todo'))
  updateData(data)
  idx = len(data)-1

if(len(args)==2):
  print(data[idx].toStr())
  sys.exit()

origin = data[idx].getTime()
symbol = args[2][:1]
if(symbol=='+' or symbol=='-'):
  isPlus = (symbol == '+')
  toAdd=args[2][1:]
  new = origin.addTime(getTime(toAdd),isPlus)
  data[idx].time= new.toStr()
  print(data[idx].toStr())
  updateData(data)
  sys.exit()


