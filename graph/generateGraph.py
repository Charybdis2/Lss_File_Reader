import matplotlib.pyplot as plt
from splits import category

MINUTE = 60

def generateGraph(c):
  x = []
  y = []
  XNoPB = []
  YNoPB = []
  for attempt in c.attempts:
    if attempt.attemptTime == None:
      continue
    else:

      xValue = int(attempt.attemptNumber)
      yValue = attempt.attemptTime.total_seconds()/MINUTE
      x.append(xValue)
      y.append(yValue)
      if attempt.isPb:
        pbX = xValue
        pbY = yValue 
      else:
        XNoPB.append(xValue)
        YNoPB.append(yValue)

  if pbX is not None and pbY is not None:
    plt.scatter(pbX, pbY, color='gold', marker='x')   
  plt.scatter(XNoPB, YNoPB, color='blue', marker='x')
  plt.plot(x, y)
  plt.xlabel("Attempt Number")
  plt.ylabel("Time")
  plt.title(f"{c.gameName}")
  filename = f"graph\{c.gameName}.png"
  plt.savefig(filename)
  plt.close()

def generateSplitGraph(c):
  numberOfSplits = len(c.splitNames)
  for i in range(numberOfSplits):
    x = []
    y = []
    XNoPB = []
    YNoPB = []
    for attempt in c.attempts:
      if attempt.attemptNumber and len(attempt.splits) > i:
        split = attempt.splits[i]
        if split.splitTime:
          xValue = int(attempt.attemptNumber)
          yValue = split.splitTime.total_seconds()/MINUTE
          if split.isPb:
            pbX = xValue
            pbY = yValue
          else:
            XNoPB.append(xValue)
            YNoPB.append(yValue)
          x.append(int(attempt.attemptNumber))
          y.append(split.splitTime.total_seconds()/MINUTE)
    if not x:
      continue

    if pbX is not None and pbY is not None:
      plt.scatter(pbX, pbY, color='gold', marker='x')   
    plt.scatter(XNoPB, YNoPB, color='blue', marker='x')
    plt.plot(x, y)
    plt.xlabel("Attempt Number")
    plt.ylabel("Time")
    plt.title(f"{c.splitNames[i]}")
    #Probably need to add some kind of split name sanitsation as characters like '?' fuck it up
    filename = f"graph\split {i}.png"
    plt.savefig(filename)
    plt.close()