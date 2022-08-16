import sys
import datetime
import utils
import log_utils
DT_NOW = datetime.datetime.now()
timeToStr = str(DT_NOW.strftime('%Y-%m-%d %H:%M:%S'))
import path
class TerminalColor:
    """ ターミナル色変更用クラス """
 
    # 代表的な色
    TODO = '\033[94m'
    PROGRESS = '\033[96m'
    DONE = '\033[92m'
    WAIT = '\033[86m'
    RESOLVED = '\033[95m'
 
    # フォントスタイル
    MARKER = '\033[7m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
 
    # 末尾制御
    _END = '\033[0m'
 
    @classmethod
    def c_print(cls, text, styles=()):
        colored_text = ""
        for style in styles:
            colored_text += style
 
        colored_text += text
        colored_text += cls._END
        print(colored_text)
 
color = {
  'todo':TerminalColor.TODO,
  'progress':TerminalColor.PROGRESS,
  'wait':TerminalColor.WAIT,
  'done':TerminalColor.DONE,
  'resolved':TerminalColor.RESOLVED
}

args = sys.argv

data = utils.getData()
if(len(args)==1):
  forExcelText = ''
  for i in range(len(data)):
    taskColor = color.get(data[i].state)
    if(taskColor==None):taskColor = TerminalColor.TODO
    my_style = [TerminalColor.BOLD,taskColor]
    TerminalColor.c_print(data[i].toStr(),my_style)

    hour = data[i].getTime().toHour()
    if(hour>0):
      forExcelText += data[i].id + ' ' + data[i].title + '\t' + str(data[i].getTime().toHour()) + '\n'
  f = open(path.Path+'forExcel.txt', 'w',encoding="utf-8")
  f.write(forExcelText)
  f.close()
  sys.exit()

taskId = utils.getTaskById(data,args[1])
if(taskId == -1):
  data.append(utils.Task(args[1],'#','-','-','0m','todo'))
  utils.updateData(data)
  taskId = len(data)-1

  content = 'none->' + data[taskId].state
  log = log_utils.Log(data[taskId].id,content,timeToStr)
  log.saveLog()

if(len(args)==2):
  font_color = color.get(data[taskId].state)
  if(font_color==None):font_color = TerminalColor.TODO
  my_style = [TerminalColor.BOLD]
  TerminalColor.c_print(data[taskId].toStr(),my_style)
  data = utils.quick_sort(data)
  utils.updateData(data)
  sys.exit()

if(args[2] == 'start'):#todo
  content = data[taskId].state + '->progress'
  log = log_utils.Log(data[taskId].id,content,timeToStr)
  log.saveLog()

  data[taskId].start = str(DT_NOW.month)+'/' + str(DT_NOW.day)
  data[taskId].state = 'progress'
  utils.updateData(data)


if(args[2] == 'delete'):#todo
  print(data[taskId].id+"を削除します。")

  content = data[taskId].state + '->none'
  log = log_utils.Log(data[taskId].id,content,timeToStr)
  log.saveLog()

  data.pop(taskId)
  
  utils.updateData(data)
  sys.exit()

symbols = []
for i in args[2:]:
  if(len(i)>1):
    symbols.append(i[:1])

if('+' in symbols or '-' in symbols):
  origin = data[taskId].getTime()
  if('+' in symbols):
    symbol = '+'
    idx = symbols.index('+')+2
    Arg=args[idx][1:]
    toAdd = utils.getTime(Arg)
  else:
    symbol = '-'
    idx = symbols.index('-')+2
    Arg=args[idx][1:]
    toAdd = utils.getTime(Arg)
    toAdd.hour *= -1
    toAdd.minute *= -1
  newTime = origin.addTime(toAdd)
  data[taskId].time= newTime.toStr()
  log = log_utils.Log(data[taskId].id,symbol+toAdd.toStr(),timeToStr)
  log.saveLog()

if('=' in symbols):
  idx = symbols.index('=')+2
  data[taskId].title = args[idx][1:]

if('?' in symbols):
  idx = symbols.index('?')+2
  oldState = data[taskId].state
  data[taskId].state= args[idx][1:]  
  content = oldState + '->' + data[taskId].state
  log = log_utils.Log(data[taskId].id,content,timeToStr)
  log.saveLog()

if(':' in symbols):
  idx = symbols.index(':')+2
  data[taskId].start = args[idx][1:]

if('~' in symbols):
  idx = symbols.index('~')+2
  data[taskId].end = args[idx][1:]

font_color = color.get(data[taskId].state)
if(font_color==None):font_color = TerminalColor.TODO
my_style = [TerminalColor.BOLD]
TerminalColor.c_print(data[taskId].toStr(),my_style)

data = utils.quick_sort(data)
utils.updateData(data)


