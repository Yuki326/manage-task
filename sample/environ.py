import sys
import os
import subprocess

UPDATE_ENVIRON_MESSAGE = '環境変数{}は既に存在します\n上書きしますか？(y/n)>'
CANCELLED_CREATE_ENVIRON_MESSAGE = '環境変数{}の作成をキャンセルしました'
CREATED_ENVIRON_MESSAGE = '環境変数{}を作成しました'

def main(key,value):
  print(os.environ.get(key))
  if(os.environ.get(key) is not None):
    doOverWrite = input(UPDATE_ENVIRON_MESSAGE.format(key))
    if(not(doOverWrite)):return
  os.environ[key] = value
  print(CREATED_ENVIRON_MESSAGE.format(key))

main(sys.argv[1],sys.argv[2])