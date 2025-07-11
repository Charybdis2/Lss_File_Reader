import matplotlib.pyplot as plt
from splits import category

MINUTE = 60

def generateGraph(c):
  x = []
  y = []
  for attempt in c.attempts:
    if attempt.attemptTime == None:
      continue
    else:
      x.append(int(attempt.attemptNumber))
      y.append(attempt.attemptTime.total_seconds()/MINUTE)
    

  plt.plot(x, y, marker='x')
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
    for attempt in c.attempts:
      if attempt.attemptNumber and len(attempt.splits) > i:
        split = attempt.splits[i]
        if split.splitTime:
          x.append(int(attempt.attemptNumber))
          y.append(split.splitTime.total_seconds()/MINUTE)
    if not x:
      continue

    plt.plot(x, y, marker='x')
    plt.xlabel("Attempt Number")
    plt.ylabel("Time")
    plt.title(f"{c.splitNames[i]}")
    #Probably need to add some kind of split name sanitsation as characters like '?' fuck it up
    filename = f"graph\split {i}.png"
    plt.savefig(filename)
    plt.close()