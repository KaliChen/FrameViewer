import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import filedialog
from tkinter import ttk

import FrameViewer.frameView as FV #(2)


import tkinter.messagebox as tkmsg
from PIL import Image, ImageTk, ImageDraw, ExifTags, ImageColor,ImageFont

import tempfile
from glob import glob
import glob

import os
from os.path import splitext
import platform



class TestTool(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Test Tool Platform:"+str(platform.system()))        

        w = 1000 # width for the Tk root
        h = 800 # height for the  Tk root

        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        '''self.notebook'''
        self.notebook = Notebook(self)
        self.notebook.pack(side = tk.TOP,fill=tk.BOTH, expand=tk.YES)


        self.init_FrameViewer()
      

 
    def init_FrameViewer(self):
        self.init_FrameViewer_tab = tk.Frame(self.notebook)
        self.init_FrameViewer_tab.pack(side = tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        self.notebook.add(self.init_FrameViewer_tab, text="init_FrameViewer")
        self.FrameSwitch = tk.StringVar()

        fvfram1 = tk.Frame(self.init_FrameViewer_tab )
        fvfram1.grid(row =0, column = 0, sticky = tk.E+tk.W)
        self.fv1 = FV.FrameViewer(fvfram1)
        fvfram1_2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram1_2.grid(row =1, column = 0, sticky = tk.E+tk.W)
        switch1 = tk.Radiobutton(fvfram1_2, text = "Frame\n Switch 1",font=('Courier', 9), variable = self.FrameSwitch, value = "Frame Switch 1", command = self.frameswitch)
        switch1.pack(side=tk.RIGHT, expand=tk.NO, fill = tk.X)

        fvfram2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram2.grid(row =2, column = 0, sticky = tk.E+tk.W)
        self.fv2 = FV.FrameViewer(fvfram2)
        fvfram2_2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram2_2.grid(row =3, column = 0, sticky = tk.E+tk.W)
        switch2 = tk.Radiobutton(fvfram2_2, text = "Frame\n Switch 2",font=('Courier', 9), variable = self.FrameSwitch, value = "Frame Switch 2", command = self.frameswitch)
        switch2.pack(side=tk.RIGHT, expand=tk.NO, fill = tk.X)
        
        fvfram3 = tk.Frame(self.init_FrameViewer_tab )
        fvfram3.grid(row =0, column = 1, sticky = tk.E+tk.W)
        self.fv3 = FV.FrameViewer(fvfram3)
        fvfram3_2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram3_2.grid(row =1, column = 1, sticky = tk.E+tk.W)
        switch3 = tk.Radiobutton(fvfram3_2, text = "Frame\n Switch 3",font=('Courier', 9), variable = self.FrameSwitch, value = "Frame Switch 3", command = self.frameswitch)
        switch3.pack(side=tk.RIGHT, expand=tk.NO, fill = tk.X)

  
        fvfram4 = tk.Frame(self.init_FrameViewer_tab )
        fvfram4.grid(row =2, column = 1, sticky = tk.E+tk.W)
        self.fv4 = FV.FrameViewer(fvfram4)
        fvfram4_2 = tk.Frame(self.init_FrameViewer_tab )
        fvfram4_2.grid(row =3, column = 1, sticky = tk.E+tk.W)
        switch4 = tk.Radiobutton(fvfram4_2, text = "Frame\n Switch 4",font=('Courier', 9), variable = self.FrameSwitch, value = "Frame Switch 4", command = self.frameswitch)
        switch4.pack(side=tk.RIGHT, expand=tk.NO, fill = tk.X)
        
    
    def frameswitch(self):
        if self.FrameSwitch.get() =="Frame Switch 1": StreamFile = self.fv1.cap#self.iv1.image_paths[self.iv1.image_idx]
        elif self.FrameSwitch.get() =="Frame Switch 2": StreamFile = self.fv2.cap#self.iv2.image_paths[self.iv2.image_idx]
        elif self.FrameSwitch.get() =="Frame Switch 3": StreamFile = self.fv3.cap#self.iv3.image_paths[self.iv3.image_idx]
        elif self.FrameSwitch.get() =="Frame Switch 4": StreamFile = self.fv4.cap#self.iv4.image_paths[self.iv4.image_idx]
        #print(StreamFile)
        """
        self.dlib_frame.cap = StreamFile
        self.frameopencv.cap = StreamFile
        """
 

if __name__ == "__main__":
       
    TT = TestTool()
    TT.mainloop()


