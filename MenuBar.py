# -*- coding: utf-8 -*-
import tkinter as tk
#from pyperclip import copy
#from time import strftime, localtime

class MenuBar:
  ###############################################
  employee_initials = "CR"
  size_of_menu_separator = 141
  SETTINGS_HEIGHT = 400
  SETTINGS_WIDTH = 350
  

  settings_menu_x_offset = 115
  settings_menu_y_offset = 25
  
  settings_State = False
  
  ###############################################
  
  def __init__(self, root):
    self.root = root
    
    root.bind('<Motion>', self.motion)
    self.menuBar = tk.Menu(self.root)
    self.createMenu()  
  
  def createMenu(self):
    settingSpacing = ''
    i = 0
    
    while i < self.size_of_menu_separator:
      settingSpacing+=" "
      i+=1
      
    self.menuBar.add_command(label=settingSpacing, state = "disabled")
    self.menuBar.add_command(label="Settings", command=self.openSettings)

    
    #Add menu to root/the main window
    self.root.config(menu=self.menuBar)
  
  def createSettingsMenu(self, root):
    """
    Creates the actual settings window.  Requires the toplevel frame, called as 'root'
    """
    
    central_Frame = tk.Frame(root)
    central_Frame.grid(column = 0, row = 1)
    bottom_Frame = tk.Frame(root)
    bottom_Frame.grid(column = 0, row = 2)
    
    self.createListOfOptions(central_Frame)
    
  def createListOfOptions(self, central_frame_of_settings_menu):
    """
    Creates the list of setting options and places it on the left most column of the given frame.
    """
    ############
    panel_coordinates = (0,0)
    panel_options = [
        "User",
        "NULL",
        "NULL"
        ]
    
    ############
    
    root = central_frame_of_settings_menu
    
    settings_panel_frame = tk.LabelFrame(root, text = "Setting Options")
    settings_panel_frame.grid(column = panel_coordinates[0], row=panel_coordinates[1])
    
    self.settings_panel = tk.Listbox(settings_panel_frame, selectmode = "SINGLE",
                                font = 10, height = 16)
    
    for item in panel_options:
      self.settings_panel.insert(tk.END, item)
    self.settings_panel.grid(column=0, row=0)
    
  
    
    
    
  def openSettings(self):
    """
    Creates a settings menu and places it on the screen using the winfo of self.root & an offset.
    
    """
    
    #######################
    
    x_offset = self.settings_menu_x_offset
    y_offset = self.settings_menu_y_offset
    
    #######################
    if not self.settings_State:  #if settings_State is False/ Window isn't opened
      self.settings = tk.Toplevel(self.root)
      self.settings.protocol("WM_DELETE_WINDOW", self.closeSettings)
      self.settings.resizable(width = tk.FALSE, height = tk.FALSE)
      
      
      x_offset += self.root.winfo_x()
      y_offset += self.root.winfo_y()
      
      self.settings_dim = "{}x{}+{}+{}".format(self.SETTINGS_WIDTH, self.SETTINGS_HEIGHT, x_offset, y_offset)
      self.settings.geometry(self.settings_dim)
      self.settings.wm_attributes("-topmost",2)
      
      self.createSettingsMenu(self.settings)
      
      self.setActive(self.settings)
      
  def closeSettings(self):
    self.settings.destroy()
    self.settings_State = False
  def setActive(self, root):
    root.lift()
    root.grab_set()
    root.focus_set()
    self.settings_State = True
  def listboxSelect(self, event):
    w = evt.
  def motion(self, event):
    global x_cord
    global y_cord
    x_cord, y_cord = event.x, event.y
    
  def null(self):
    """
    Empty function for his and/or her pleasure.
    """
    pass
  
