import config
import sys

import os
import excel_util
import task_util
import log_util
import common_util
COMPLETED_SETUP_MESSAGE = 'セットアップが完了しました。'
EMPTY_TASK_MESSAGE = '表示するタスクが存在しません'
def output(tasks,id=None):
  if(id is None):
    task_util.printTaskList(tasks)
  else:
    tasks[id].colorPrint()
  task_util.updateTasks(tasks)
  excel_util.outputForExcel(tasks)

def addFiles():
  for i in config.TEXT_FILES:
    f = open(config.PATH+'/'+i, 'a')
    f.write('')
    f.close()

def setup():
  if(not(os.path.exists(config.PATH))):
      os.mkdir(config.PATH)
  addFiles()

def main(input):
  input.pop(0)

  tasks = task_util.getTasks()
  if(input==[]):
    if(tasks==[]):common_util.error(EMPTY_TASK_MESSAGE)
    tasks = common_util.quick_sort(tasks,task_util.cmpState)
    output(tasks)
    sys.exit()
  
  if(input[0] == 'setup'):
    setup()
    print(COMPLETED_SETUP_MESSAGE)
    sys.exit()

  taskId = task_util.getTaskById(tasks,input[0])
  if(taskId == -1):
    tasks.append(task_util.getNewTask(input[0]))
    log_util.recordChangeState(tasks[taskId].id,'none','todo')

  input.pop(0)
  if(input==[]):
    tasks = common_util.quick_sort(tasks,task_util.cmpState)
    output(tasks,taskId)
    sys.exit()

  if(input[0] is 'delete'):
    ans = input(tasks[taskId].id+"を削除しますか？(y,n)->")
    if(ans is 'n'):sys.exit()
    log_util.recordChangeState(tasks[taskId].id,tasks[taskId].state,'none')
    tasks.pop(taskId)
    tasks = common_util.quick_sort(tasks,task_util.cmpState)
    task_util.updateTasks(tasks)
    sys.exit()

  changedTask = tasks[taskId].changeTaskByInput(input)
  tasks[taskId] = changedTask

  tasks = common_util.quick_sort(tasks,task_util.cmpState)
  output(tasks,taskId)

args = sys.argv # コマンドライン引数を取得
main(args)