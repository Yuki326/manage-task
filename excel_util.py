import path

def getTextForExcel(task):
  forExcelText = ''
  hour = task.getTime().toHour()
  if(hour>0):
    forExcelText += task.id + ' ' + task.title + '\t' + str(task.getTime().toHour()) + '\n'
  return forExcelText
  
def outputForExcel(tasks):
  text = ''
  for task in tasks:
      text += getTextForExcel(task)
  f = open(path.Path+'forExcel.txt', 'w',encoding="utf-8")
  f.write(text)
  f.close()