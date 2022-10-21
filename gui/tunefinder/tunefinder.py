import tkinter as tk
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

    __findLabel = Label(__root, text="Search for a song: ", bd=1)
    __findSong = Entry(__root, bg="#14e8f7")

    __searchBtn = Button(__root, text="Search")
    __topSongs = Label(text="Top 5 Songs", bg="RED")

    def __init__(self, **kwargs):
        
        try:
            self.__winWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__winHeight = kwargs['height']
        except KeyError:
            pass
        
        
        #Centers window on screen
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        
        left = (screenWidth / 2) - (self.__winWidth / 2)

        top = (screenHeight / 2) - (self.__winHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__winWidth, self.__winHeight, left, top))

        #Adds Title attribute defined above
        self.__root.title(f"{self.__winTitle}")


        
        self.__findLabel.grid(row=0, column=0, sticky=E+W)
        self.__findSong.grid()
        self.__searchBtn.grid()
        self.__searchBtn.config(command=self.__findSong)

        self.__topSongs.grid(row=0, column=1, rowspan=3, sticky=N+S)
    
    def __searchSong(self):
        findsong = self.__findSong.get()
        response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=5&term={str(findsong)}")
        res = response.json()
       
        songs = []
        for item in res["results"]:
            songs.append(item["trackName"])


        for i, song in enumerate(songs, 1):
            print(f"Num {i}: {song}")
            


    def run(self):
        self.__root.mainloop()

    

tune = tuneFinder(width=800, height=600)
tune.run()