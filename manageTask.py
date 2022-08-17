import sys
import excel_util

import time_util
import task_util
import log_util
import common_util

args = sys.argv # コマンドライン引数を取得

tasks = task_util.getTasks()

args.pop(0)
if(len(args)==[]):
  task_util.printTaskList(tasks)
  excel_util.outputForExcel(tasks)
  sys.exit()

taskId = task_util.getTaskById(tasks,args[0])
if(taskId == -1):
  tasks.append(task_util.getNewTask(tasks[taskId].id))
  taskId = len(tasks)-1

  log_util.recordChange(tasks[taskId].id,'none','todo')

args.pop(0)
if(len(args)==[]):
  tasks[taskId].colorPrint()
  task_util.updateTasks(tasks)
  sys.exit()

if(args[0] == 'delete'):#todo
  print(tasks[taskId].id+"を削除します。")

  log_util.recordChange(tasks[taskId].id,tasks[taskId].state,'none')

  tasks.pop(taskId)
  
  task_util.updateTasks(tasks)
  sys.exit()

symbols = common_util.getSymbols(args)

if('start' in symbols):#todo
  log_util.recordChange(tasks[taskId].id,tasks[taskId].state,'progress')

  tasks[taskId].start = time_util.getSimpleDate()
  tasks[taskId].state = 'progress'

if('+' in symbols or '-' in symbols):
  origin = tasks[taskId].getTime()
  if('+' in symbols):
    symbol = '+'
    idx = symbols.index('+')
    Arg=args[idx][1:]
    toAdd = time_util.convertTime(Arg)
  else:
    symbol = '-'
    idx = symbols.index('-')
    Arg=args[idx][1:]
    toAdd = time_util.convertTime(Arg)
    toAdd *= -1
  
  newTime = origin.addTime(toAdd)
  tasks[taskId].time= newTime.toStr()
  logToSave = log_util.Log(tasks[taskId].id,symbol+toAdd.toStr(),time_util.DT_NOW_TO_SHOW)
  logToSave.saveLog()

if('=' in symbols):
  idx = symbols.index('=')
  tasks[taskId].title = args[idx][1:]

if('?' in symbols):
  idx = symbols.index('?')
  tasks[taskId].state= args[idx][1:]

  oldState = tasks[taskId].state
  log_util.recordChange(tasks[taskId].id,oldState,tasks[taskId].state)


if(':' in symbols):
  idx = symbols.index(':')
  tasks[taskId].start = args[idx][1:]

if('~' in symbols):
  idx = symbols.index('~')
  tasks[taskId].end = args[idx][1:]

tasks[taskId].colorPrint()

task_util.updateTasks(tasks)