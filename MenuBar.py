# -*- coding: utf-8 -*-
import tkinter as tk
import etc.setting_Data as sd
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
    
    self.config = sd.setting_Data()
        
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
    panel_options = []
    
    #Pulls data from the config file to create a list of settings.
    tmp = self.config.return_Raw_Settings()
    for setting in tmp:
      panel_options.append(setting)
    ############
    

    central_Frame = tk.Frame(root, width = self.SETTINGS_WIDTH-50)
    central_Frame.grid(column = 0, row = 0, padx = 5, sticky = 'w')
    #central_Frame.grid_propagate(False)
    
    bottom_Frame = tk.Frame(root, width = self.SETTINGS_WIDTH, height = 100)
    bottom_Frame.grid(column = 0, row = 1, padx = 5)
    bottom_Frame.grid_propagate(False)

    self.createListOfOptions(central_Frame, listbox_coordinates, panel_options)
    self.createSelectedForm(central_Frame, form_coordinates) 
    self.createButtonFrame(bottom_Frame)
    
    #Initialized what to load when Settings is created.
    self.settings_panel.select_set(0)
    self.list_Of_Setting_Frames['User'].mountFrame()
    
  def createListOfOptions(self, central_frame_of_settings_menu, panel_cords, panel_options):
    """
    Creates the list of setting options and places it on the left most column of the given frame.
    """
    
    root = central_frame_of_settings_menu
    
    settings_panel_frame = tk.LabelFrame(root, text = "Setting Options")
    settings_panel_frame.grid(column = panel_cords[0], row=panel_cords[1], sticky="w")
    
    self.settings_panel = tk.Listbox(settings_panel_frame, selectmode = "SINGLE",
                                font = 10, height = 16, width = 10, exportselection = False)
    
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
    """
    Creates an object 'grouped_Settings' and stores within this class.  This object is used to handle
    necessary setting Objects within a dict.  
    
    list_Of_Setting_Frames stores the dict returned by grouped_Settings.
    """
    self.grouped_Settings = all_Settings(root, self.config)
    self.list_Of_Setting_Frames = self.grouped_Settings.return_Settings_Dict()
    
  def createButtonFrame(self, root):
    button_Frame = tk.Frame(root, width=self.SETTINGS_WIDTH)
    button_Frame.grid(column=0, row=0)
    
    self.apply = tk.Button(button_Frame, text="Apply", command= self.grouped_Settings.save_All)
    
    
    self.apply.grid()
    
    pass
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
    try:
      index = (int(item.curselection()[0]))
      value = item.get(index)
      
      for setting_frame in self.list_Of_Setting_Frames:
        if setting_frame == value:
          self.list_Of_Setting_Frames[setting_frame].mountFrame()
        else:
          self.list_Of_Setting_Frames[setting_frame].unmountFrame()
    except:
      pass
    
  def motion(self, event):
    global x_cord
    global y_cord
    x_cord, y_cord = event.x, event.y
    
  def null(self):
    """
    Empty function for his and/or her pleasure.
    """
    pass
  
class all_Settings:
  def __init__(self, root, configuration_File):
    """
    all_Settings stores all setting Objects within itself.  Used to call the list of setting Objects and
    write to each object.  Essentially handles the load of object handling away from the main settings Class.
    
    """
    
    #Settings are created and stored in local variables.  Class initializations are handled below.
    user_Frame = user_Settings(root, configuration_File)
    null_Frame = null_Settings_TEST(root, configuration_File)
    
    list_of_Settings = [
        user_Frame,
        null_Frame
        ]
    #Configuration data pulled from a JSON file is stored within this object.
    self.config = configuration_File
    
    #A dict containing each setting Object is stored within this object.
    
    self.dict_Of_Setting_Frames = {}
    #keys = self.config.return_List_Of_Keys
    i = 0
    
    #Cycles through the list of settings created by the Setting_Data module.
    #Creates a tmp dict and saves the result within the object.
    #IMPORTANT:
    #Settings listed within list_of_Settings MUST MATCH the list of returned keys perfectly.
    
    for setting_Label in self.config.return_List_Of_Keys():
      tmp = {setting_Label: list_of_Settings[i]}
      self.dict_Of_Setting_Frames.update(tmp)
      i+=1
      

  def return_Settings_Dict(self):
    """
    Returns the dict containing every setting Object.
    """
    return self.dict_Of_Setting_Frames
  def save_All(self): #TO DO
    master = self.config.return_Raw_Settings()
    for setting in self.dict_Of_Setting_Frames:
      pass
  
  ##### Baseline functions for settings ######
class base_settings:
  def __init__(self, root, config):
    self.config = config
    self.setting_Attribute = ""
    self.user_data = {}
        
    self.master = tk.Frame(root)
    self.form = tk.Frame(self.master)
    self.form.grid(sticky = "nsew", padx = 8, pady=8)
    
  def unmountFrame(self):
    self.master.grid_forget()
  def mountFrame(self):
    self.master.grid()
  def save_Settings(self):
    self.config.write_Specified_Setting(self.setting_Attribute, self.user_data)
  #############################################
  
  ##### Setting Item: User ######
  
class user_Settings(base_settings):
  def __init__(self, root, config):
    super().__init__(root, config)
    ############################
    
    self.setting_Attribute = "User" #name of the setting
    self.user_data = self.config.return_Specified_Setting(self.setting_Attribute)
    
    self.initials = tk.StringVar()
    self.employeeNum = tk.StringVar()
    ############################
    
    self.createForm()
    
  def createForm(self):
    initials_label = tk.Label(self.form, text = "Initials")
    self.initials_textbox = tk.Entry(self.form, width=5, textvariable= self.initials)
    emp_label = tk.Label(self.form, text = "Employee Number")
    self.emp_textbox = tk.Entry(self.form, width = 5, textvariable = self.employeeNum)
    initials_label.grid(column=0, row=0, sticky = 'w')
    self.initials_textbox.grid(column=1, row=0, sticky = 'w')
    emp_label.grid(column=0, row=1)
    self.emp_textbox.grid(column=1,row=1)
  
    self.populateFields()
    
  def populateFields(self):
    items = self.user_data
    self.initials.set(items['Initials'])
    self.employeeNum.set(items['Emp_Num'])
  
    
class null_Settings_TEST(base_settings):
  def __init__(self, root, config):
    super().__init__(root, config)    
    test = tk.Label(self.form, text = "Placeholder for debugging")
    test.grid()
    
    
  
  
  ###############################
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
