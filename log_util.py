import path
import time_util

class Log:
  id = ''
  content = ''
  #comment
  time = ''
  def __init__(self,id,content,time ):
      self.id = id
      self.content = content
      self.time = time

  def toStr(self):
    text = '{} {} {}\n'
    return text.format(self.id,self.content,self.time )

  def saveLog(self):
    f = open(path.Path+'log.txt', 'a',encoding="utf-8")
    f.write(self.toStr())
    f.close()

def recordChange(id,oldState,newState):
  content = oldState + '->' + newState
  logToSave = Log(id,content,time_util.DT_NOW_TO_SHOW)
  logToSave.saveLog()