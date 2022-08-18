import sys

import excel_util
import task_util
import log_util
import common_util

def main(input):
  tasks = task_util.getTasks()

  input.pop(0)
  if(input==[]):
    tasks = common_util.quick_sort(tasks,task_util.cmpState)
    task_util.updateTasks(tasks)
    task_util.printTaskList(tasks)
    excel_util.outputForExcel(tasks)
    sys.exit()

  taskId = task_util.getTaskById(tasks,input[0])
  if(taskId == -1):
    tasks.append(task_util.getNewTask(tasks[taskId].id))
    taskId = len(tasks)-1

    log_util.recordChangeState(tasks[taskId].id,'none','todo')

  input.pop(0)
  if(input==[]):
    tasks = common_util.quick_sort(tasks,task_util.cmpState)
    tasks[taskId].colorPrint()
    task_util.updateTasks(tasks)
    sys.exit()

  if(input[0] == 'delete'):#todo
    print(tasks[taskId].id+"を削除します。")

    log_util.recordChangeState(tasks[taskId].id,tasks[taskId].state,'none')

    tasks.pop(taskId)

    tasks = common_util.quick_sort(tasks,task_util.cmpState)
    task_util.updateTasks(tasks)
    sys.exit()

  changedTask = tasks[taskId].changeTaskByInput(input)
  tasks[taskId] = changedTask

  tasks[taskId].colorPrint()
  tasks = common_util.quick_sort(tasks,task_util.cmpState)
  task_util.updateTasks(tasks)

args = sys.argv # コマンドライン引数を取得
main(args)