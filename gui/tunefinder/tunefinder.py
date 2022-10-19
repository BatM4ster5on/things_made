import tkinter as tk
from urllib import response
import requests
import os
import json
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class tuneFinder:

    __root = Tk()

    __winWidth = 300
    __winHeight = 300
    __labelVar = StringVar()
    __winTitle = ("TuneFinder | AgM ")
    __winMenuBar = Menu(__root)

    __findLabel = Label(__root, text="Search for a song: ")
    __songName = Entry(__root, bg="#14e8f7", )

    __searchBtn = Button(__root, text="Search")

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


        
        self.__findLabel.grid()
        self.__songName.grid()
        self.__searchBtn.grid()
        self.__searchBtn.config(command=self.__searchSong)
    
    def __searchSong(self):
        songname = self.__songName.get()
        response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + str(songname))
        res = response.json()
        for result in res["results"]:
            print(result["trackName"])

    def run(self):
        self.__root.mainloop()

    

tune = tuneFinder(width=800, height=600)
tune.run()