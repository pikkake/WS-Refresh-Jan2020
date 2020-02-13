import os
from util import openJSON, writeJSON

class setting_Data:
  """
  Module for creating the raw JSON file associated with the program.
  
  
  """
  path = "config\\config.json"
  JSON = {}
  User = {}
  
  def __init__(self, file_stream = "config\\config.json"):

    if not os.path.exists('config'):
      os.mkdir('config')
    try:
      if not os.path.isfile(file_stream):
        self.resetSettings()   
        self.write()
      else:
        self.JSON = openJSON(file_stream)
        self.path = file_stream
    except Exception as e: print(e)

  
  def resetSettings(self):
    self.User = {
      "Name":"",
      "Initials":"",
      "Emp_Num": 0
      
      }
    
    self.JSON['User'] = self.User
  ###EDIT THIS LATER
  def write(self):
    self.JSON['User'] = self.User
    writeJSON(self.JSON, self.path)
  def return_Specified_Setting(self, setting_Name):
    return self.JSON[setting_Name]
  def return_Raw_Settings(self):
    return self.JSON
  def write_Settings(self, setting_Label, raw_Buffer, master_JSON):
    master_JSON[setting_Label] = raw_Buffer
    writeJSON(master_JSON, self.path)
  def printJSON(self):
    print(self.JSON)
