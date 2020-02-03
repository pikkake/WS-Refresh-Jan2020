# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import scrolledtext
from run import *
from util import strip_input, clear
from time import localtime, strftime, sleep
from pyperclip import copy
import os

#https://likegeeks.com/python-gui-examples-tkinter-tutorial/
#https://effbot.org/tkinterbook/tkinter-application-windows.htm
#https://www.python-course.eu/tkinter_layout_management.php
#http://epydoc.sourceforge.net/stdlib/Tkinter.Variable-class.html


class wsRefresh:
  ##############################################################
  APP_TITLE = "Jan 2020 WS Refresh Call Formatter v0.81"
  MIN_APP_WIDTH = 500
  MIN_APP_HEIGHT = 400  #420 for footer inclusion
  banner_color = '#3B4483 '
  bg_theme = '#E1E1E1'
  fg_theme = 'black'
  button_bg = '#dedede'
  button_fg = 'black'
  button_active_bg = '#c9c9c9'
  button_active_fg = 'black'
  employee_code = ""
  employee_initials = ""
  
  ##############################################################
  outputDict = {
    "S-":"",
    "Name: ":"",
    "Phone: ":"",
    "Workstations":[
      {"WS-":"", "Old: ":"", "New: ":""}, #WS-1 index 0
      {"WS-":"", "Old: ":"", "New: ":""}, #WS-2
      {"WS-":"", "Old: ":"", "New: ":""}, #WS-3
      {"WS-":"", "Old: ":"", "New: ":""}  #WS-4
      ]
    }
  output_string = []
  
  def __init__(self, root):
    i = 0
    while i < 15:
      self.output_string.append("")
      i += 1
    
    self.root = root
    root.resizable(width = FALSE, height = FALSE)

    #root.iconbitmap('ico/icon.ico')
    root.resizable(width = FALSE, height = FALSE)
    self.storeNum = StringVar()
    self.entryName = StringVar()
    self.techPhone = StringVar()
    self.WS_1 = StringVar()
    self.oldMAC_1 = StringVar()
    self.newMAC_1 = StringVar()
    self.WS_2 = StringVar()
    self.oldMAC_2 = StringVar()
    self.newMAC_2 = StringVar()
    self.WS_3 = StringVar()
    self.oldMAC_3 = StringVar()
    self.newMAC_3 = StringVar()
    self.WS_4 = StringVar()
    self.oldMAC_4 = StringVar()
    self.newMAC_4 = StringVar()
    self.release_code = StringVar()
    
    self.initials = StringVar()
    self.emp_code = StringVar()

    self.createTraceStatements()

    self.dim = "{}x{}".format(self.MIN_APP_WIDTH, self.MIN_APP_HEIGHT)
    self.root.geometry(self.dim)
    self.root.title(self.APP_TITLE)
    self.root.wm_attributes("-topmost",1)
    
    self.WS_refresh_buttonBar = Frame(root, width = 600, height = 31, bg=self.banner_color)
    #Allows the frame to expand to the set width and height
    self.WS_refresh_buttonBar.grid_propagate(False)
    
    self.WS_Center = Frame(root, bg = self.bg_theme)
    self.WS_refresh_buttonBar.grid(sticky=E+W)
    self.WS_Center.grid(row=1, sticky='nsew')
    
    self.WS_Bottom = Frame(root, relief = SUNKEN, borderwidth=1, width = self.MIN_APP_WIDTH, height = 20)
    self.WS_Bottom.grid_propagate(False)
    self.WS_Bottom.grid(row=2, sticky='w')
    
    self.WS_refresh_form = Frame(self.WS_Center, bg = self.bg_theme)
    self.WS_refresh_textarea = Frame(self.WS_Center, bg = self.bg_theme)
    self.WS_refresh_form.grid(column=0, row=0,padx = 5, pady = 10, sticky ='NW')
    self.WS_refresh_textarea.grid(column=1, row = 0, padx=15, pady=10, sticky='NW')
  
    self.KDS_TS_Btn = Button(self.WS_refresh_buttonBar, text="KDS Timestamp", command = self.KDS_Changer_TS, bg = self.button_bg, fg = self.button_fg, activebackground=self.button_active_bg, activeforeground=self.button_active_fg)
    self.KDS_TS_Btn.grid(column=0, row=0, padx=10)
    self.Comment_TS_Btn = Button(self.WS_refresh_buttonBar, text = "Comment Timestamp", command = self.comment_TS, bg = self.button_bg, fg = self.button_fg, activebackground=self.button_active_bg, activeforeground=self.button_active_fg)
    self.Comment_TS_Btn.grid(column=1, row=0)
    seperator = Frame(self.WS_refresh_buttonBar, width = 10)
    seperator.grid_propagate(False)
    seperator.grid(column = 2, padx=23)
    
    self.clearFrame = Frame(self.WS_refresh_buttonBar, bg = self.banner_color)
    self.clearFrame.grid(column=3, row = 0, padx=15, sticky='nsew')
    
    self.clear_all = Button(self.clearFrame, text="Clear Only", command = self.clearForm, bg='#ebdb34', fg='#0d0d0c', activebackground='#ccbe2d', activeforeground='#0d0d0c')
    self.clear_all.grid(column=0, row = 0, padx=18, sticky='E')
    self.clear_all = Button(self.clearFrame, text="Clear & Log", command = self.clearAndLog, bg='#C1392B', fg='#F8F8F8', activebackground='#a3382a', activeforeground='#F8F8F8')
    self.clear_all.grid(column=1, row = 0, padx=2, pady=3, sticky='E')
    
    self.createForm(self.WS_refresh_form)
    self.createTextBox(self.WS_refresh_textarea)
    
    self.createFooter(self.WS_Bottom)
    
    
    
  def createForm(self, root):
    self.info = Frame(root, bg = self.bg_theme)
    self.ws_1 = Frame(root, pady=5, bg = self.bg_theme)
    self.ws_2 = Frame(root, pady=5, bg = self.bg_theme)
    self.ws_3= Frame(root, pady=5, bg = self.bg_theme)
    self.ws_4= Frame(root, pady=5, bg = self.bg_theme)
    
    #Labels for the form
    self.store_label = Label(self.info, text = "Store: ", bg = self.bg_theme, fg = self.fg_theme)
    self.name_label = Label(self.info, text = "Name: ", bg = self.bg_theme, fg = self.fg_theme)
    self.phone_label = Label(self.info, text = "Phone: ", bg = self.bg_theme, fg = self.fg_theme)
    self.WS_label_1 = Label(self.ws_1, text = "WS-1: ", bg = self.bg_theme, fg = self.fg_theme)
    self.oldMAC_label_1 = Label(self.ws_1, text = "Old MAC: ", bg = self.bg_theme, fg = self.fg_theme)
    self.newMAC_label_1 = Label(self.ws_1, text = "New MAC: ", bg = self.bg_theme, fg = self.fg_theme)
    self.WS_label_2 = Label(self.ws_2, text = "WS-2: ", bg = self.bg_theme, fg = self.fg_theme)
    self.oldMAC_label_2 = Label(self.ws_2, text = "Old MAC: ", bg = self.bg_theme, fg = self.fg_theme)
    self.newMAC_label_2 = Label(self.ws_2, text = "New MAC: ", bg = self.bg_theme, fg = self.fg_theme)
    self.WS_label_3 = Label(self.ws_3, text = "WS-3: ", bg = self.bg_theme, fg = self.fg_theme)
    self.oldMAC_label_3 = Label(self.ws_3, text = "Old MAC: ", bg = self.bg_theme, fg = self.fg_theme)
    self.newMAC_label_3 = Label(self.ws_3, text = "New MAC: ", bg = self.bg_theme, fg = self.fg_theme)
    self.WS_label_4 = Label(self.ws_4, text = "WS-4: ", bg = self.bg_theme, fg = self.fg_theme)
    self.oldMAC_label_4 = Label(self.ws_4, text = "Old MAC: ", bg = self.bg_theme, fg = self.fg_theme)
    self.newMAC_label_4 = Label(self.ws_4, text = "New MAC: ", bg = self.bg_theme, fg = self.fg_theme)
    #Place labels into the grid
    
    
    self.info.grid(column=0,row=0, sticky='w')
    self.ws_1.grid(column=0, row=1, sticky='w')
    self.ws_2.grid(column=0, row=2, sticky='w')
    self.ws_3.grid(column=0, row=3, sticky='w')
    self.ws_4.grid(column=0, row=4, sticky='w')
    
    self.store_label.grid(column=0,row=0, sticky='W')
    self.name_label.grid(column=0,row=1, sticky='W')
    self.phone_label.grid(column=0,row=2, sticky='W')
    
    self.WS_label_1.grid(column=0,row=0, sticky='W')
    self.oldMAC_label_1.grid(column=0,row=1, sticky='W')
    self.newMAC_label_1.grid(column=0,row=2, sticky='W')
    self.WS_label_2.grid(column=0,row=1, sticky='W')
    self.oldMAC_label_2.grid(column=0,row=2, sticky='W')
    self.newMAC_label_2.grid(column=0,row=3, sticky='W')
    self.WS_label_3.grid(column=0,row=1, sticky='W')
    self.oldMAC_label_3.grid(column=0,row=2, sticky='W')
    self.newMAC_label_3.grid(column=0,row=3, sticky='W')
    self.WS_label_4.grid(column=0,row=1, sticky='W')
    self.oldMAC_label_4.grid(column=0,row=2, sticky='W')
    self.newMAC_label_4.grid(column=0,row=3, sticky='W')
    
    #Entry boxes for the WS project
    self.store_txtBox = Entry(self.info, width=5, textvariable = self.storeNum)
    self.name_txtBox = Entry(self.info, width=20, textvariable =self.entryName)
    self.phone_txtBox = Entry(self.info, width=16, textvariable =self.techPhone)
    
    self.WS_txtBox_1 = Entry(self.ws_1, width=12, textvariable= self.WS_1)
    self.oldMAC_txtBox_1 = Entry(self.ws_1, width=18, textvariable= self.oldMAC_1)
    self.newMAC_txtBox_1= Entry(self.ws_1, width=18, textvariable= self.newMAC_1)
    self.WS_txtBox_2 = Entry(self.ws_2, width=12, textvariable= self.WS_2)
    self.oldMAC_txtBox_2 = Entry(self.ws_2, width=18, textvariable= self.oldMAC_2)
    self.newMAC_txtBox_2= Entry(self.ws_2, width=18, textvariable= self.newMAC_2)
    self.WS_txtBox_3 = Entry(self.ws_3, width=12, textvariable= self.WS_3)
    self.oldMAC_txtBox_3 = Entry(self.ws_3, width=18, textvariable= self.oldMAC_3)
    self.newMAC_txtBox_3= Entry(self.ws_3, width=18, textvariable= self.newMAC_3)
    self.WS_txtBox_4 = Entry(self.ws_4, width=12, textvariable= self.WS_4)
    self.oldMAC_txtBox_4 = Entry(self.ws_4, width=18, textvariable= self.oldMAC_4)
    self.newMAC_txtBox_4= Entry(self.ws_4, width=18, textvariable= self.newMAC_4)
    
    #Place entries on the grid
    self.store_txtBox.grid(column=1, row=0, sticky="w")
    self.name_txtBox.grid(column=1,row=1, sticky="w")
    self.phone_txtBox.grid(column=1,row=2, sticky="w")
    
    self.WS_txtBox_1.grid(column=1,row=0, sticky="w")
    self.oldMAC_txtBox_1.grid(column=1,row=1, sticky="w")
    self.newMAC_txtBox_1.grid(column=1,row=2, sticky="w")
    self.WS_txtBox_2.grid(column=1,row=1, sticky="w")
    self.oldMAC_txtBox_2.grid(column=1,row=2, sticky="w")
    self.newMAC_txtBox_2.grid(column=1,row=3, sticky="w")
    self.WS_txtBox_3.grid(column=1,row=1, sticky="w")
    self.oldMAC_txtBox_3.grid(column=1,row=2, sticky="w")
    self.newMAC_txtBox_3.grid(column=1,row=3, sticky="w")
    self.WS_txtBox_4.grid(column=1,row=1, sticky="w")
    self.oldMAC_txtBox_4.grid(column=1,row=2, sticky="w")
    self.newMAC_txtBox_4.grid(column=1,row=3, sticky="w")
  def createTextBox(self, root):
    self.entryBoxes = Frame(root, bg = self.bg_theme)
    self.textbox = Frame(root, bg = self.bg_theme)
    self.buttons = Frame(root, bg = self.bg_theme)
    self.identifiers = Frame(root, bg = self.bg_theme)
      
    self.entryBoxes.grid(column=0,row=0, sticky='W')
    self.release_label = Label(self.entryBoxes, text="Release Code:")
    #self.release_label.grid(column=0, row=0, sticky="w")
    self.release_Button = Button(self.entryBoxes, text = "Release Code", command = self.setReleaseCode, bg = self.button_bg, fg = self.button_fg, activebackground=self.button_active_bg, activeforeground=self.button_active_fg)
    self.release_Button.grid(column=0, row=0)
    self.release_entry = Entry(self.entryBoxes, width = 12, textvariable = self.release_code)
    self.release_entry.grid(column=1, row=0, padx=5)
    
    self.textbox.grid(column=0,row=1, pady=2)
    self.txt = scrolledtext.ScrolledText(self.textbox,width=30,height=15)
    self.txt.grid(column=0, row=0)
    
    self.buttons.grid(column=0,row=2)
    self.copyTextBox = Button(self.buttons, text="Copy All", command = self.copyText, bg = self.button_bg, fg = self.button_fg, activebackground=self.button_active_bg, activeforeground=self.button_active_fg)
    self.copyTextBox.grid(column=2, row=0, sticky='E', padx=5)
    self.formatOutput = Button(self.buttons, text="Format", command = self.formatOutput, bg = self.button_bg, fg = self.button_fg, activebackground=self.button_active_bg, activeforeground=self.button_active_fg)
    self.formatOutput.grid(column = 0, row = 0, padx=5)
    self.logButton = Button(self.buttons, text="Log Call", command = self.logCall, bg = self.button_bg, fg = self.button_fg, activebackground=self.button_active_bg, activeforeground=self.button_active_fg)
    self.logButton.grid(column = 1, row = 0, padx=5)
    
    self.identifiers.grid(column=0, row=3, sticky='w', pady=5)
    self.initials_label = Label(self.identifiers, text="Initials:", bg = self.bg_theme, fg = self.fg_theme)
    self.initials_entry = Entry(self.identifiers, width = 6, textvariable = self.initials)  
    self.emp_code_label = Label(self.identifiers, text = "Emp Code:", bg = self.bg_theme, fg = self.fg_theme)
    self.emp_code_entry = Entry(self.identifiers, width = 6, textvariable = self.emp_code)
    
    self.initials_label.grid(column = 0, row = 0, sticky='w')
    self.initials_entry.grid(column = 1, row = 0, sticky='w')
    self.emp_code_label.grid(column=0, row=1, sticky='w')
    self.emp_code_entry.grid(column=1, row=1, sticky='w')
  def createFooter(self, root):
    self.footerFrame1 = Frame(root)
    self.footerFrame1.grid(sticky='e')
    
    self.footerMsg = Label(self.footerFrame1)
    self.footerMsg.grid(sticky='e')
  """def alterFooter(self, msg):
    self.footerMsg.config(text = msg)
    sleep(5)
    self.footerMsg.config(text = "")"""
  def copyText(self):
    copy(self.txt.get("1.0", END).strip())
  def setReleaseCode(self, cp = True):
    store_code = self.store_txtBox.get()
    if len(store_code) != 0:
      if len(store_code) == 1:

        tmp = "000"+store_code
      elif len(store_code) == 2:
        tmp = "00"+store_code
      elif len(store_code) == 3:
        tmp = "0"+store_code
      else:
        tmp = store_code
        
      self.release_entry.delete(0,END)
      
      global employee_code
      release = self.employee_code + strftime("%m%d", localtime()) + tmp
      self.release_entry.insert(0, release) 
      if cp == True:
        copy(release)
  def clearAndLog(self):
    self.logCall()
    self.clearForm()
    pass
  def clearForm(self):
    self.store_txtBox.delete(0,'end')
    self.name_txtBox.delete(0,'end')
    self.phone_txtBox.delete(0,'end')
    self.WS_txtBox_1.delete(0,'end')
    self.oldMAC_txtBox_1.delete(0,'end')
    self.newMAC_txtBox_1.delete(0,'end')
    self.WS_txtBox_2.delete(0,'end')
    self.oldMAC_txtBox_2.delete(0,'end')
    self.newMAC_txtBox_2.delete(0,'end')
    self.WS_txtBox_3.delete(0,'end')
    self.oldMAC_txtBox_3.delete(0,'end')
    self.newMAC_txtBox_3.delete(0,'end')
    self.WS_txtBox_4.delete(0,'end')
    self.oldMAC_txtBox_4.delete(0,'end')
    self.newMAC_txtBox_4.delete(0,'end')
    self.release_entry.delete(0, END)
    self.txt.delete("1.0", END)
    i = 0
    while i < 15:
      self.output_string[i] = ""
      i+=1
    
    
    pass
  def logCall(self):
    path = "logs\\"
    timestamp = strftime("20%y-%m-%d.rtf", localtime())
    path+= timestamp
    try:
      if len(self.txt.get('1.0',END)) > 1:
        f = open(path, 'a+')
        f.write(strftime("=== %m/%d/20%y %I:%M:%S %p ===\n",localtime()))
        f.write(self.txt.get('1.0', END)+"\n")
        f.close()
    except:
      pass
  def createLogTimestamp(self):
    pass
  def createTraceStatements(self):
    
    self.storeNum.trace('w', self.setStore)
    self.entryName.trace('w', self.setName)
    self.techPhone.trace('w',self.setPhone)
    
    self.WS_1.trace('w', self.setWS_one)
    self.oldMAC_1.trace('w', self.setOld_MAC_one)
    self.newMAC_1.trace('w', self.setNew_MAC_one)

    self.WS_2.trace('w', self.setWS_two)
    self.oldMAC_2.trace('w', self.setOld_MAC_two)
    self.newMAC_2.trace('w', self.setNew_MAC_two)

    self.WS_3.trace('w', self.setWS_three)
    self.oldMAC_3.trace('w', self.setOld_MAC_three)
    self.newMAC_3.trace('w', self.setNew_MAC_three)
    
    self.WS_4.trace('w', self.setWS_four)
    self.oldMAC_4.trace('w', self.setOld_MAC_four)
    self.newMAC_4.trace('w', self.setNew_MAC_four)    
    
    self.initials.trace('w', self.setInitials)
    self.emp_code.trace('w', self.setEmp_Code)
  def setInitials(self, *args):
    #self.initials = self.initials_entry.get().upper()
    self.s_init = self.initials_entry.get()
    global employee_initials
    if len(self.s_init) > 4: 
      self.initials.set(self.s_init[:4].upper())
  
    else:
      self.initials.set(self.s_init[:4].upper())
    
    self.employee_initials = self.initials_entry.get().upper()

  def setEmp_Code(self, *args):
    self.s_emp = self.emp_code_entry.get()
    if len(self.s_emp) > 2: self.emp_code.set(self.s_emp[:2])
    global employee_code
    self.employee_code = self.emp_code.get()
    
  def setStore(self, *args):
    self.s_num = self.storeNum.get()
    if len(self.s_num) > 4: self.storeNum.set(self.s_num[:4])
    
    if len(self.s_num) != 0:
      if len(self.s_num) == 1:
        tmp = "000"+self.s_num
      elif len(self.s_num) == 2:
        tmp = "00"+self.s_num
      elif len(self.s_num) == 3:
        tmp = "0"+self.s_num
      else:
        tmp = self.s_num
      self.outputDict["S-"] = tmp
      self.output_string[0] = "S-"+ tmp
    else:
      self.outputDict["S-"] = ""
      self.output_string[0] = "S-"
  def setName(self, *args):
    self.s_name = self.entryName.get().title().strip()
    self.outputDict["Name: "] = self.s_name
    self.output_string[1] = "Name: "+self.s_name
  def setPhone(self, *args):
    self.s_phone = self.techPhone.get().strip()
    self.outputDict["Phone: "] = self.s_phone
    self.output_string[2] = self.s_phone
    
  def setWS_one(self, *args):
    self.s_WS_one = self.WS_1.get().upper().strip()
    self.outputDict["Workstations"][0]["WS-"] = self.s_WS_one
    if self.s_WS_one != "":
      self.output_string[3] = "WS-"+ self.s_WS_one
  def setOld_MAC_one(self, *args):
    self.s_oldMAC_one = self.oldMAC_1.get().upper().strip()
    self.outputDict["Workstations"][0]["Old: "] = self.s_oldMAC_one
    self.output_string[4] = self.s_oldMAC_one
  def setNew_MAC_one(self, *args):
    self.s_newMAC_one = self.newMAC_1.get().upper().strip()
    self.outputDict["Workstations"][0]["New: "] = self.s_newMAC_one
    self.output_string[5] = self.s_newMAC_one
    
  def setWS_two(self, *args):
    self.s_WS_two = self.WS_2.get().upper().strip()
    self.outputDict["Workstations"][1]["WS-"] = self.s_WS_two
    if self.s_WS_two != "":
      self.output_string[6] = "WS-"+ self.s_WS_two
  def setOld_MAC_two(self, *args):
    self.s_oldMAC_two = self.oldMAC_2.get().upper().strip()
    self.outputDict["Workstations"][1]["Old: "] = self.s_oldMAC_two
    self.output_string[7] = self.s_oldMAC_two
  def setNew_MAC_two(self, *args):
    self.s_newMAC_two = self.newMAC_2.get().upper().strip()
    self.outputDict["Workstations"][1]["New: "] = self.s_newMAC_two
    self.output_string[8] = self.s_newMAC_two
    
  def setWS_three(self, *args):
    self.s_WS_three = self.WS_3.get().upper().strip()
    self.outputDict["Workstations"][2]["WS-"] = self.s_WS_three
    if self.s_WS_three != "":
      self.output_string[9] = "WS-"+ self.s_WS_three
  def setOld_MAC_three(self, *args):
    self.s_oldMAC_three = self.oldMAC_3.get().upper().strip()
    self.outputDict["Workstations"][2]["Old: "] = self.s_oldMAC_three
    self.output_string[10] = self.s_oldMAC_three
  def setNew_MAC_three(self, *args):
    self.s_newMAC_three = self.newMAC_3.get().upper().strip()
    self.outputDict["Workstations"][2]["New: "] = self.s_newMAC_three
    self.output_string[11] = self.s_newMAC_three  
    
  def setWS_four(self, *args):
    self.s_WS_four = self.WS_4.get().upper().strip()
    self.outputDict["Workstations"][3]["WS-"] = self.s_WS_four
    if self.s_WS_four != "":
      self.output_string[12] = "WS-"+ self.s_WS_four
  def setOld_MAC_four(self, *args):
    self.s_oldMAC_four = self.oldMAC_4.get().upper().strip()
    self.outputDict["Workstations"][3]["Old: "] = self.s_oldMAC_four
    self.output_string[13] = self.s_oldMAC_four
  def setNew_MAC_four(self, *args):
    self.s_newMAC_four = self.newMAC_4.get().upper().strip()
    self.outputDict["Workstations"][3]["New: "] = self.s_newMAC_four
    self.output_string[14] = self.s_newMAC_four
    
  def formatPhone(self, phone):
    try:
      if len(phone) == 10:
        phone = phone[:3] + "-" + phone[3:6]+"-"+phone[6:]
        return phone
      elif len(phone) == 12:
        if '-' not in phone:
          phone = phone[2:5] + "-" + phone[5:8]+"-"+phone[8:]
          return phone
        else:
          return phone
      elif phone == "store":
        phone = "- Called From Store"
        return phone    
      else:
        return phone
      self.outputDict["Phone: "] = phone 
    except:
      return phone
  def formatMAC(self, mac):
    try:
      split_mac = mac.split(":")
      mac = ""
      for i in split_mac:
        mac += i
      return mac
    except:
      return mac
  def formatOutput(self):
    self.txt.delete("1.0", END)
    i = 0
    for item in self.output_string:
      #print(str(i)+", "+item) #for debugging
      if item != "":
        if i == 0:
          self.txt.insert(INSERT, item)
        elif i == 2:
          self.txt.insert(INSERT, "\nPhone: " + self.formatPhone(item))
        elif i == 4 or i == 7 or i == 10 or i == 13:        
          self.txt.insert(INSERT, "\nOld: " + self.formatMAC(item))
        elif i == 6 or i == 9 or i == 12:
          self.txt.insert(INSERT, "\n\n"+item)
        elif i == 5 or i == 8 or i == 11 or i == 14:
          self.txt.insert(INSERT, "\nNew: " + self.formatMAC(item))
        else:
          self.txt.insert(INSERT,"\n"+item)
      i+=1
      self.setReleaseCode(cp = False)
  def KDS_Changer_TS(self):
    #msg = "KDS Timestamp copied to clipboard"
    clipboard = self.employee_initials + " " + strftime("%I:%M%p", localtime())
    copy(clipboard)
    
    #self.alterFooter(msg)
  def comment_TS(self):
    clipboard = strftime("%m/%d @%I:%M%p ("+self.employee_initials+") ", localtime())
    copy(clipboard)
if __name__ == "__main__":
  
  root = Tk()
  ws_gui = wsRefresh(root)
  
  root.mainloop()