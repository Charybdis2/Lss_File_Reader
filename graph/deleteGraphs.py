import os
import glob

def deleteGraphs():
  files = glob.glob(os.path.join("graph", "*.png"))
  for file in files:
    try:
      os.remove(file)
    except Exception as e:
      print(f"Could not delete files {e}")