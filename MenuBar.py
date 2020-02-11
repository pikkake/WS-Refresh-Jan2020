# -*- coding: utf-8 -*-
import tkinter as tk
#from pyperclip import copy
#from time import strftime, localtime

class MenuBar:
  
  """
  Requires a main window with dimensions 500x400px.  
  IF changing dimensions, edit the 'size_of_menu' parameter
  
  """
  ###############################################
  employee_initials = "CR"    #Initials of the employee
  
  SETTINGS_HEIGHT = 400       #Height of the settings window
  SETTINGS_WIDTH = 350        #Width of the settings window
  
  size_of_menu_separator = 141  #Space that pushes the settings button to the right
  settings_menu_x_offset = 115  #Offset from the top left corner of the main window
  settings_menu_y_offset = 25
  
  settings_State = False        #Boolean handling if Settings is open
  
  list_Of_Setting_Frames = {}
  
  ###############################################
  
  def __init__(self, root):
    self.root = root
    
    root.bind('<Motion>', self.motion)
    self.menuBar = tk.Menu(self.root)
    self.createMenuBar()  
  
  def createMenuBar(self):
    settingSpacing = ''
    i = 0
    
    while i < self.size_of_menu_separator:
      settingSpacing+=" "
      i+=1
      
    self.menuBar.add_command(label=settingSpacing, state = "disabled")
    
    #Settings button runs the openSettings function
    self.menuBar.add_command(label="Settings", command=self.openSettings)

    
    #Add menu to root/the main window
    self.root.config(menu=self.menuBar)
  
  def createSettingsMenu(self, root):
    """
    Creates the actual settings window.  Requires the toplevel frame, called as 'root'
    """
    ############
    listbox_coordinates = (0,0) #column/row
    form_coordinates = (1,0)
    panel_options = [
        "User",
        "NULL"
        ]
    ############
    

    central_Frame = tk.Frame(root)
    central_Frame.grid(column = 0, row = 0)
    bottom_Frame = tk.Frame(root)
    bottom_Frame.grid(column = 0, row = 2)
    
    self.createListOfOptions(central_Frame, listbox_coordinates, panel_options)
    self.createSelectedForm(central_Frame, form_coordinates)
    
    
  def createListOfOptions(self, central_frame_of_settings_menu, panel_cords, panel_options):
    """
    Creates the list of setting options and places it on the left most column of the given frame.
    """
    
    root = central_frame_of_settings_menu
    
    settings_panel_frame = tk.LabelFrame(root, text = "Setting Options")
    settings_panel_frame.grid(column = panel_cords[0], row=panel_cords[1], sticky="nsew")
    
    self.settings_panel = tk.Listbox(settings_panel_frame, selectmode = "SINGLE",
                                font = 10, height = 16, width = 10)
    
    for item in panel_options:
      self.settings_panel.insert(tk.END, item)
    self.settings_panel.grid(column=0, row=0)
    
    self.settings_panel.bind('<<ListboxSelect>>', self.listboxSelect)
    
    
  def createSelectedForm(self, central_frame_of_settings_menu, form_cords) :
    """
    Creates the area which the forms are changed.
    Takes the central frame of the settings windows and assigned it locally as 'root,'
    Uses coordinates passed from the createSettingsMenu to place it in the frame.
    
    """
    root = central_frame_of_settings_menu
    
    self.form_frame = tk.Frame(root)
    self.form_frame.grid(column = form_cords[0], row=form_cords[1], sticky="nsew")
    
    self.createIndividual_Setting_Frames(self.form_frame)
    
    
  def createIndividual_Setting_Frames(self, root):

    user = user_Settings(root)
    null = null_Settings_TEST(root)
    
    self.list_Of_Setting_Frames = {
        "User": user,
        "NULL": null
        }
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
      
      settings_dim = "{}x{}+{}+{}".format(self.SETTINGS_WIDTH, self.SETTINGS_HEIGHT, x_offset, y_offset)
      self.settings.geometry(settings_dim)
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
    item = event.widget
    index = (int(item.curselection()[0]))
    value = item.get(index)
    
    for setting_frame in self.list_Of_Setting_Frames:
      if setting_frame == value:
        self.list_Of_Setting_Frames[setting_frame].mountFrame()
      else:
        self.list_Of_Setting_Frames[setting_frame].unmountFrame()
    
  def motion(self, event):
    global x_cord
    global y_cord
    x_cord, y_cord = event.x, event.y
    
  def null(self):
    """
    Empty function for his and/or her pleasure.
    """
    pass
  
  ##### Baseline functions for settings ######
class base_settings:
  def __init__(self, root):
    self.master = tk.Frame(root)
    self.form = tk.Frame(self.master)
    self.form.grid(sticky = "nsew", padx = 8, pady=8)
    
  def unmountFrame(self):
    self.master.grid_forget()
  def mountFrame(self):
    self.master.grid()
  #############################################
  
  ##### Setting Item: User ######
  
class user_Settings(base_settings):
  def __init__(self, root):
    super().__init__(root)
    ############################
    
    
    self.initials = tk.StringVar()
    self.employeeNum = tk.StringVar()
    ############################
    
    
    
    self.createForm()
    
  def createForm(self):
    initials_label = tk.Label(self.form, text = "Initials")
    initials_textbox = tk.Entry(self.form, width=5, textvariable= self.initials)
    emp_label = tk.Label(self.form, text = "Employee Number")
    emp_textbox = tk.Entry(self.form, width = 5, textvariable = self.employeeNum)
    initials_label.grid(column=0, row=0, sticky = 'w')
    initials_textbox.grid(column=1, row=0, sticky = 'w')
    emp_label.grid(column=0, row=1)
    emp_textbox.grid(column=1,row=1)
    
    
    
class null_Settings_TEST(base_settings):
  def __init__(self, root):
    super().__init__(root)    
    test = tk.Label(self.form, text = "Null Setting")
    test.grid()
    
    
  
  
  ###############################
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
