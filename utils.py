import sys
Path = '~/Desktop/dev/atomica/manage-task/Record/'

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
    hourS = minuteS = '0'
    if('h' in self.time):
      hourS = self.time.split('h')[0]
      if('m' in self.time):
        minuteS = self.time.split('h')[1].split('m')[0]
    else:
      minuteS = int(self.time.split('m')[0])
    errorMessage = '無効な引数です。:'+self.time
    if(hourS.isdecimal()):
      res.hour = int(hourS)
    else:common.error(errorMessage)
    if(minuteS.isdecimal()):
      res.minute = int(minuteS)
    else:common.error(errorMessage)
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
  f = open(Path+'test.txt', 'w',encoding="utf-8")#ファイルの中身が消えるので注意
  f.write(text)
  f.close()

def getTaskById(data,id):
  for i in range(len(data)):
    if data[i].id == id:
      return i
  return -1

def getTime(str):
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
    else:common.error(errorMessage)
    if(minuteS.isdecimal()):
      res.minute = int(minuteS)
    else:common.error(errorMessage)
    return res

def cmpState(s1,s2):
  lst = ['progress','todo','wait','done','resolved']
  n1 = n2 = 100
  if(s1 in lst):
    n1 = lst.index(s1)
  if(s2 in lst):
    n2 = lst.index(s2)
  if(n1<n2):
    return 1
  elif(n1>n2):
    return -1
  else:
    return 0
  
# クイックソートを行う関数
def quick_sort(x):
    # 基準値を抽出(半分の位置の値)
    n = len(x)
    pivot = x[int(n / 2)]
 
    # i番目の値と基準値を比較して左l、右r、真ん中mに追加
    l = []
    r = []
    m = []
    for i in range(n):
        sample = x[i]
        if cmpState(sample.state,pivot.state)==1:
            l.append(sample)
        elif cmpState(sample.state,pivot.state)==-1:
            r.append(sample)
        else:
            m.append(sample)
    # lとrの場合でそれぞれ再帰処理による分割を行う
    if l:
        l = quick_sort(l)
    if r:
        r = quick_sort(r)
    return l + m + r
