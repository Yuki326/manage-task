import sys
def error(e):
  print(e)
  sys.exit()

def getSymbols(args):
    symbols = []
    for arg in args:
        if(arg== 'start'):
            symbols.append(arg)
        if(len(arg)>1):
            symbols.append(arg[:1])
    return symbols
  
# クイックソートを行う関数
def quick_sort(x,cmp):
    # 基準値を抽出(半分の位置の値)
    n = len(x)
    pivot = x[int(n / 2)]
 
    # i番目の値と基準値を比較して左l、右r、真ん中mに追加
    l = []
    r = []
    m = []
    for i in range(n):
        sample = x[i]
        if cmp(sample,pivot)==1:
            l.append(sample)
        elif cmp(sample,pivot)==-1:
            r.append(sample)
        else:
            m.append(sample)
    # lとrの場合でそれぞれ再帰処理による分割を行う
    if l:
        l = quick_sort(l,cmp)
    if r:
        r = quick_sort(r,cmp)
    return l + m + r
