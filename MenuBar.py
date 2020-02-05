# -*- coding: utf-8 -*-
import tkinter as tk
from pyperclip import copy
from time import strftime, localtime

class MenuBar:
  employee_initials = "CR"
  
  def __init__(self, root):
    
    
    self.createMenu(root)
    pass
  
  
  def createMenu(self, root):
    self.menubar = tk.Menu(root)
    self.menubar.add_command(label="KDS Timestamp", command=self.KDS_Changer_TS)
    
    self.menubar.add_command(label="Commept Timestamp", command=self.comment_TS)
    self.multipleMenuSeparator()
    self.menubar.add_command(label="Settings", command=self.null)
    root.config(menu=self.menubar)
  pass
  def null(self):
    pass
  def KDS_Changer_TS(self):
    #msg = "KDS Timestamp copied to clipboard"
    clipboard = self.employee_initials + " " + strftime("%I:%M%p", localtime())
    copy(clipboard)
    
    #self.alterFooter(msg)
  def comment_TS(self):
    clipboard = strftime("%m/%d @%I:%M%p ("+self.employee_initials+") ", localtime())
    copy(clipboard)
  def multipleMenuSeparator(self):
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
    self.menubar.add_separator()
