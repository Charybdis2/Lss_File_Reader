import xml.etree.ElementTree as ET
from .splits import splits
from .timeParse import timeParse
'''
This class is the individual attempts, holds the splits and total time of the attempt and if it is a pb or not
'''
class attempt():
  def __init__(self, isPb):
    self.attemptNumber = ""
    self.isPb = isPb
    self.attemptTime = 0
    self.splits = []
  
  def setAttempt(self, root):
    self.attemptNumber = root.attrib.get("id")
    if root.find("RealTime") is not None:
      self.attemptTime = timeParse(root.find("RealTime").text)
    else:
      self.attemptTime = None
  
  def setSplits(self, root):
    for i in root.iter("Segment"):
      history = i.find("SegmentHistory")
      if history is not None:
          for t in history.findall("Time"):
              if t.attrib.get("id") == self.attemptNumber:
                  bestTime = i.find("BestSegmentTime/RealTime")
                  thisTime = t.find("RealTime")
                  if bestTime is not None and thisTime is not None:
                      self.splits.append(splits(thisTime.text, bestTime.text == thisTime.text))