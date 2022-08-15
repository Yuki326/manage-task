Path = '~/Desktop/dev/atomica/manage-task/Record/'
class Log:
  id = ''
  content = ''
  time = ''
  def __init__(self,id,content,time ):
      self.id = id
      self.content = content
      self.time = time

  def toStr(self):
    text = '{} {} {}\n'
    return text.format(self.id,self.content,self.time )

  def saveLog(self):
    f = open(Path+'log.txt', 'a',encoding="utf-8")
    f.write(self.toStr())
    f.close()