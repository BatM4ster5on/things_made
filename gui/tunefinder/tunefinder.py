import tkinter as tk
import os
import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class tuneFinder:

    __root = Tk()

    __winWidth = 300
    __winHeight = 300
    __winTitle = ("TuneFinder | AgM ")
    __winMenuBar = Menu(__root)


    __findSong = Entry(__root, bg="#52f2ea", )



    def __init__(self, **kwargs):
        
        try:
            self.__winWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__winHeight = kwargs['height']
        except KeyError:
            pass
        

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        
        left = (screenWidth / 2) - (self.__winWidth / 2)

        top = (screenHeight / 2) - (self.__winHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__winWidth, self.__winHeight, left, top))

        
        self.__root.title(f"{self.__winTitle}")


        self.__findSong.grid(sticky="ew")



    def run(self):
        self.__root.mainloop()

    

tune = tuneFinder(width=800, height=600)
tune.run()