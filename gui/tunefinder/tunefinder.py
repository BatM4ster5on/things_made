import requests
import os
import json
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class tuneFinder:

    __root = Tk()
    __winWidth, __winHeight = 300, 300

    # __labelVar = StringVar()
    __winTitle = ("TuneFinder | AgM ")
    #Not using menu bar yet
    # __winMenuBar = Menu(__root)
    
    __songFrame = LabelFrame(__root, text="Search For a Song bellow!", bd=4, bg="#23543c", padx=50, pady=50)
    # __findLabel = Label(__songFrame, text="Search for a song: ", bd=1)
    __findSong = Entry(__songFrame, bg="#14e8f7")

    __searchBtn = Button(__songFrame, text="Search")

    __outputFrame = LabelFrame(__root, text="Output Frame")
    __outputSongs = Label(__outputFrame, text="")

    __topSongs = Label(__songFrame, text="Top 5 Songs", bg="#207349")

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


        #LabelFrames
        self.__songFrame.grid(row=0, column=0, sticky=E+W, ipadx=50, ipady=50)
        self.__outputFrame.grid(row=0, column=1, columnspan=2, sticky=N+S, ipadx=170, ipady=50)

        # self.__findLabel.grid(row=0, column=0, sticky=E+W)
        self.__findSong.grid(row=0, column=0, columnspan=3, sticky=E+W)
        self.__searchBtn.grid(row=1, column=0, sticky=E+W)
        self.__searchBtn.config(command=self.__searchSong)

        self.__topSongs.grid(row=0, column=3, rowspan=3, sticky=N+S)
    
    def __searchSong(self):
        findsong = self.__findSong.get()
        response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=5&term={str(findsong)}")
        res = response.json()
       
    
        songs = [item["trackName"] for item in res["results"]]
       


        for i, song in enumerate(songs, 1):
            song_output = Label(self.__songFrame, text=f"{i}: {song}")
            song_output.grid()
            


    def run(self):
        self.__root.mainloop()

    

tune = tuneFinder(width=800, height=600)
tune.run()