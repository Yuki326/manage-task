import path
import time_util

class Log:
  id = ''
  content = ''
  comment = ''
  time = ''
  def __init__(self,id,content,comment,time ):
      self.id = id
      self.content = content
      self.comment = comment
      self.time = time

  def toStr(self):
    text = '{} {} {} {}\n'
    return text.format(self.id,self.content,self.comment,self.time )

  def saveLog(self):
    f = open(path.Path+'log.txt', 'a',encoding="utf-8")
    f.write(self.toStr())
    f.close()

def record(id,content,comment=''):
  logToSave = Log(id,content,comment,time_util.DT_NOW_TO_SHOW)
  logToSave.saveLog()

def recordChangeState(id,oldState,newState):
  content = oldState + '->' + newState
  record(id,content)
