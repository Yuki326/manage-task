class TerminalColor:
    """ ターミナル色変更用クラス """
 
    # 代表的な色
    TODO = '\033[94m'
    PROGRESS = '\033[96m'
    DONE = '\033[92m'
    WAIT = '\033[86m'
    RESOLVED = '\033[95m'
    ERROR = '\033[31m'
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
 
colorTypes = {
  'todo':TerminalColor.TODO,
  'progress':TerminalColor.PROGRESS,
  'wait':TerminalColor.WAIT,
  'done':TerminalColor.DONE,
  'resolved':TerminalColor.RESOLVED
}
def colorPrint(content,fontColor):
  if(fontColor==None):fontColor = TerminalColor.TODO
  my_style = [TerminalColor.BOLD,fontColor]
  TerminalColor.c_print(content,my_style)