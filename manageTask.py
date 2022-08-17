import sys
import datetime
from .excel_util import outputForExcel

import path
import time_util
import task_util
import log_util
import color_util

DT_NOW = datetime.datetime.now()
timeToShow = str(DT_NOW.strftime('%Y-%m-%d %H:%M:%S'))

args = sys.argv

tasks = task_util.getTasks()
if(len(args)==1):
  # tasks.printTaskList()
  for task in tasks:
    # task.colorPrint()
    taskColor = color_util.colorTypes.get(task.state)
    color_util.colorPrint(task.toStr(),taskColor)

  outputForExcel(tasks)
  sys.exit()

taskId = task_util.getTaskById(tasks,args[1])
if(taskId == -1):
  # createDefaultTask
  tasks.append(task_util.Task(args[1],'#','-','-','0m','todo'))
  task_util.updateTasks(tasks)
  taskId = len(tasks)-1

  # recordAction(ACTION.CREATETASK)
  content = 'none->' + tasks[taskId].state
  logToSave = log_util.Log(tasks[taskId].id,content,timeToShow)
  logToSave.saveLog()

if(len(args)==2):
  taskColor = color_util.colorTypes.get(tasks[taskId].state)
  color_util.printC(tasks[taskId].toStr(),taskColor)

  task_util.updateTasks(tasks)
  sys.exit()

if(args[2] == 'delete'):#todo
  print(tasks[taskId].id+"を削除します。")

  content = tasks[taskId].state + '->none'
  logToSave = log_util.Log(tasks[taskId].id,content,timeToShow)
  logToSave.saveLog()

  tasks.pop(taskId)
  
  task_util.updateTasks(tasks)
  sys.exit()

symbols = []
for i in args[2:]:
  if(i == 'start'):
    symbols.append(i)
  if(len(i)>1):
    symbols.append(i[:1])

if('start' in symbols):#todo
  content = tasks[taskId].state + '->progress'
  logToSave = log_util.Log(tasks[taskId].id,content,timeToShow)
  logToSave.saveLog()

  tasks[taskId].start = str(DT_NOW.month)+'/' + str(DT_NOW.day)
  tasks[taskId].state = 'progress'

if('+' in symbols or '-' in symbols):
  origin = tasks[taskId].getTime()
  if('+' in symbols):
    symbol = '+'
    idx = symbols.index('+')+2
    Arg=args[idx][1:]
    toAdd = time_util.convertTime(Arg)
  else:
    symbol = '-'
    idx = symbols.index('-')+2
    Arg=args[idx][1:]
    toAdd = time_util.convertTime(Arg)
    toAdd.hour *= -1
    toAdd.minute *= -1
  newTime = origin.addTime(toAdd)
  tasks[taskId].time= newTime.toStr()
  logToSave = log_util.Log(tasks[taskId].id,symbol+toAdd.toStr(),timeToShow)
  logToSave.saveLog()

if('=' in symbols):
  idx = symbols.index('=')+2
  tasks[taskId].title = args[idx][1:]

if('?' in symbols):
  idx = symbols.index('?')+2
  oldState = tasks[taskId].state
  tasks[taskId].state= args[idx][1:]  
  content = oldState + '->' + tasks[taskId].state
  logToSave = log_util.Log(tasks[taskId].id,content,timeToShow)
  logToSave.saveLog()

if(':' in symbols):
  idx = symbols.index(':')+2
  tasks[taskId].start = args[idx][1:]

if('~' in symbols):
  idx = symbols.index('~')+2
  tasks[taskId].end = args[idx][1:]

taskColor = color_util.colorTypes.get(tasks[taskId].state)
color_util.printC(tasks[i].toStr(),taskColor)

task_util.updateTasks(tasks)


