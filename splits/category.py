import xml.etree.ElementTree as ET
from .attempt import attempt
from .timeParse import timeParse
'''
This acts as the a class for the entire .lss file 
'''
class category():
  def __init__(self):
    self.gameName = ""
    self.gameCategory = ""
    self.numberOfAttempts = 0
    self.splitNames = []
    self.attempts = []
    self.root = ""
    self.pb = None
    self.pbID = None
  
  def parseFile(self, file):
    self.root = ET.parse(file)
    #Sets the general class attributes
    self.gameName = self.root.find("GameName").text
    self.gameCategory = self.root.find("CategoryName").text
    for name in self.root.iter("Segment"):
      self.splitNames.append((name.find("Name").text))
    self.numberOfAttempts = self.root.find("AttemptCount").text

    attemptHistoryRoot = self.root.find("AttemptHistory")
    self.pb = None
    self.pbID = None

    for attemptNode in attemptHistoryRoot.findall("Attempt"):
        realTimeNode = attemptNode.find("RealTime")
        if realTimeNode is not None:
            currentTime = timeParse(realTimeNode.text)
            if self.pb is None or currentTime < self.pb:
                self.pb = currentTime
                self.pbID = attemptNode.attrib.get("id")
    

    for attemptNode in attemptHistoryRoot.findall("Attempt"):
        isPb = (attemptNode.attrib.get("id") == self.pbID)
        thisAttempt = attempt(isPb)
        thisAttempt.setAttempt(attemptNode)
        thisAttempt.setSplits(self.root)
        self.attempts.append(thisAttempt)