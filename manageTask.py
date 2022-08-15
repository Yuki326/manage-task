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

class Task:
  
   # コンストラクタ
  def __init__(self, id, title, time, state):
    self.id = id
    self.title = title
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
    return text.format(self.id, self.title,self.time,self.state)

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
          tmp.title=areas[i]
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
taskId = getTaskById(data,args[1])
if(taskId == -1):
  data.append(Task(args[1],'#','0m','todo'))
  updateData(data)
  taskId = len(data)-1

if(len(args)==2):
  print(data[taskId].toStr())
  sys.exit()

if(args[2] == 'start'):#todo
  updateData(data)
  sys.exit()

symbols = []
for i in args[2:]:
  symbols.append(i[:1])
print(symbols)
if('+' in symbols or '-' in symbols):
  origin = data[taskId].getTime()
  if('+' in symbols):
    idx = symbols.index('+')+2
    Arg=args[idx][1:]
    toAdd = getTime(Arg)
  else:
    idx = symbols.index('-')+2
    Arg=args[idx][1:]
    toAdd = getTime(Arg)
    toAdd.hour *= -1
    toAdd.minute *= -1
  new = origin.addTime(toAdd)
  data[taskId].time= new.toStr()
  updateData(data)

if('=' in symbols):
  idx = symbols.index('=')+2
  data[taskId].title = args[idx][1:]
  updateData(data)

if('?' in symbols):
  print("a\n")
  idx = symbols.index('?')+2
  data[taskId].state= args[idx][1:]
  updateData(data)

# :start ~end
print(data[taskId].toStr())
