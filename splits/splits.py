from datetime import timedelta
from .timeParse import timeParse

class splits():
  def __init__(self, splitTime, isPb):
    self.splitTime = timeParse(splitTime)
    self.isPb = isPb
  
