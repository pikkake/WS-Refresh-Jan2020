# -*- coding: utf-8 -*-
import tkinter as tk
#from pyperclip import copy
#from time import strftime, localtime

class MenuBar:
  ###############################################
  employee_initials = "CR"
  size_of_menu_separator = 141
  SETTINGS_HEIGHT = 100
  SETTINGS_WIDTH = 100
  
  
  ###############################################
  
  def __init__(self, root):
    
    root.bind('<Motion>', self.motion)
    self.menuBar = tk.Menu(root)
    self.createMenu(root)  
  
  def createMenu(self, root):
    settingSpacing = ''
    i = 0
    
    while i < self.size_of_menu_separator:
      settingSpacing+=" "
      i+=1
      
    self.menuBar.add_command(label=settingSpacing, state = "disabled")
    self.menuBar.add_command(label="Settings", command=lambda: self.openSettings(root))
    self.createSettingsMenu(root)
    
    #Add menu to root/the main window
    root.config(menu=self.menuBar)
  pass
  def createSettingsMenu(self, root):
    self.settings = tk.Toplevel(root)
    self.settings.protocol("WM_DELETE_WINDOW", self.settings.withdraw)
    self.settings.resizable(width = tk.FALSE, height = tk.FALSE)
    self.settings_dim = "{}x{}".format(self.SETTINGS_WIDTH, self.SETTINGS_HEIGHT)
    self.settings.geometry(self.settings_dim)
    self.settings.wm_attributes("-topmost",2)
    
    display = tk.Label(self.settings,text = "Test")
    display.grid()  
    self.settings.withdraw()
    
  def openSettings(self, root):
    self.settings.geometry()
    self.settings.deiconify()
    
  def motion(self, event):
    global x_cord
    global y_cord
    x_cord, y_cord = event.x, event.y
    
  def null(self):
    """
    Empty function for his and/or her pleasure.
    """
    pass
  
