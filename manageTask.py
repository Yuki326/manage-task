import sys
import datetime
import utils
args = sys.argv
if(len(args)==1):
  print('コマンドライン引数を入力してください')
  sys.exit()

data = utils.getData()
taskId = utils.getTaskById(data,args[1])
if(taskId == -1):
  data.append(utils.Task(args[1],'#','-','-','0m','todo'))
  utils.updateData(data)
  taskId = len(data)-1

if(len(args)==2):
  print(data[taskId].toStr())
  sys.exit()

if(args[2] == 'start'):#todo
  dt_now = datetime.datetime.now()
  data[taskId].start = str(dt_now.month)+'/' + str(dt_now.day)
  utils.updateData(data)
  print(data[taskId].toStr())
  sys.exit()

symbols = []
for i in args[2:]:
  symbols.append(i[:1])

if('+' in symbols or '-' in symbols):
  origin = data[taskId].getTime()
  if('+' in symbols):
    idx = symbols.index('+')+2
    Arg=args[idx][1:]
    toAdd = utils.getTime(Arg)
  else:
    idx = symbols.index('-')+2
    Arg=args[idx][1:]
    toAdd = utils.getTime(Arg)
    toAdd.hour *= -1
    toAdd.minute *= -1
  new = origin.addTime(toAdd)
  data[taskId].time= new.toStr()

if('=' in symbols):
  idx = symbols.index('=')+2
  data[taskId].title = args[idx][1:]

if('?' in symbols):
  idx = symbols.index('?')+2
  data[taskId].state= args[idx][1:]

if(':' in symbols):
  idx = symbols.index(':')+2
  data[taskId].start = args[idx][1:]

if('~' in symbols):
  idx = symbols.index('~')+2
  data[taskId].end = args[idx][1:]
# :start ~end
utils.updateData(data)

print(data[taskId].toStr())
