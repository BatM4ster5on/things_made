import tkinter as tk
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *






class Calculator:

    __root = Tk()


    __calcWidth = 315
    __calcHeight = 450
    __calcTitle = ("AGM | Calculator")
    __primeInput = tk.Entry(__root, bg="#abd8e0", justify="right",  font=24, borderwidth=4)
    __calcMenuBar = Menu(__root)
    # __calcBtnArea = 
    


    __button_1 = Button(__root, text="1", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)
    __button_2 = Button(__root, text="2", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)
    __button_3 = Button(__root, text="3", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)

    __button_4 = Button(__root, text="4", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)
    __button_5 = Button(__root, text="5", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)
    __button_6 = Button(__root, text="6", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)

    __button_7 = Button(__root, text="7", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)
    __button_8 = Button(__root, text="8", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)
    __button_9 = Button(__root, text="9", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)
    
    __button_0 = Button(__root, text="0", justify="center", bg="#b4c0d4", padx=40, pady=20, font=16, border=4)
    __button_cls = Button(__root, text="Clear", justify="center", bg="#b4c0d4", padx=80, pady=20, font=16, border=4)


   


    def __init__(self, **kwargs):
        
        try:
            self.__calcWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__calcHeight = kwargs['height']
        except KeyError:
            pass
        

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        
        left = (screenWidth / 2) - (self.__calcWidth / 2)

        top = (screenHeight / 2) - (self.__calcHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__calcWidth, self.__calcHeight, left, top))

        
        self.__root.title(f"{self.__calcTitle}")

        self.__primeInput.grid(row=0, column=0, columnspan=3, ipady=20, sticky='ew')

        self.__calcMenuBar.add_cascade(label="File")

        self.__root.config(menu=self.__calcMenuBar)

        def num_click(number):

            value = self.__primeInput.get()
            self.__primeInput.delete(0, END)
            self.__primeInput.insert(0, str(value) + str(number))

        # Number Buttons 1-9
        self.__button_1.grid(row=3, column=0)
        self.__button_1.config(command=lambda: num_click(1))

        self.__button_2.grid(row=3, column=1)
        self.__button_2.config(command=lambda: num_click(2))

        self.__button_3.grid(row=3, column=2)
        self.__button_3.config(command=lambda: num_click(3))


        self.__button_4.grid(row=2, column=0)
        self.__button_4.config(command=lambda: num_click(4))

        self.__button_5.grid(row=2, column=1)
        self.__button_5.config(command=lambda: num_click(5))
        
        self.__button_6.grid(row=2, column=2)
        self.__button_6.config(command=lambda: num_click(6))


        self.__button_7.grid(row=1, column=0)
        self.__button_7.config(command=lambda: num_click(7))
        
        self.__button_8.grid(row=1, column=1)
        self.__button_8.config(command=lambda: num_click(8))

        self.__button_9.grid(row=1, column=2)
        self.__button_9.config(command=lambda: num_click(9))


        self.__button_0.grid(row=4, column=2)
        self.__button_0.config(command=lambda: num_click(0))


        self.__button_cls.grid(row=4, column=0, columnspan=2)
        

    def run(self):
        self.__root.mainloop()

    

calc = Calculator(width=320, height=450)
calc.run()