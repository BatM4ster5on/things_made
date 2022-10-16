import tkinter as tk
import os
from tkinter import *

# To get the space above for message
from tkinter.messagebox import *

# To get the dialog box to open when required
from tkinter.filedialog import *


class Notepad:
    __root = Tk()

    __winWidth = 300
    __winHeight = 300
    __winTitle = ("Untitled | NotePad")
    __winTextArea = tk.Text(__root, relief=tk.RAISED, bg='green')
    __winMenuBar = Menu(__root)
    __winFileMenu = Menu(__winMenuBar, tearoff=0)
    __winEditMenu = Menu(__winMenuBar, tearoff=0)
    __winHelpMenu = Menu(__winMenuBar, tearoff=0)

    # winMenuBar =

    __winScrollBar = Scrollbar(__winTextArea)
    __file = None

    def __init__(self, **kwargs):

        try:
            self.__winWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__winHeight = kwargs['height']
        except KeyError:
            pass

        self.__root.title(f"{self.__winTitle}")

        self.__winTextArea.grid(sticky="nsew")

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__winWidth / 2)

        top = (screenHeight / 2) - (self.__winHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__winWidth,
                                              self.__winHeight,
                                              left, top))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__winScrollBar.pack(side=RIGHT, fill=Y)

        self.__winScrollBar.config(command=self.__winTextArea.yview)
        self.__winTextArea.config(yscrollcommand=self.__winScrollBar.set)

        #File Menu
        self.__winFileMenu.add_command(label="Save", command=self.__saveFile)

        self.__winFileMenu.add_command(label="Open", command=self.__openFIle)

        self.__winFileMenu.add_command(label="Word Counter", command=self.__counter)



        #creates a horizontal margin
        self.__winFileMenu.add_separator()
        self.__winFileMenu.add_command(label="Exit", command=self.__quitApp)


        self.__winMenuBar.add_cascade(label="File", menu=self.__winFileMenu)

        
        #EditMenu

        self.__winEditMenu.add_command(label="Cut", command=self.__cut)

        self.__winEditMenu.add_command(label="Copy", command=self.__copy)

        self.__winEditMenu.add_command(label="Paste", command=self.__paste)

        self.__winMenuBar.add_cascade(label="Edit", menu=self.__winEditMenu)

        #Help menu
        self.__winHelpMenu.add_command(label="About", command=self.__winAbout)

        self.__winMenuBar.add_cascade(label="Help", menu=self.__winHelpMenu)

        self.__root.config(menu=self.__winMenuBar)


    def __quitApp(self):
        self.__root.destroy()

    #HelpMenu
    def __winAbout(self):
        showinfo("NotePad", "By AGM aka TonyDanza")


    # FileMenu
    def __saveFile(self):

        if self.__file == None:
            self.__file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                                            ("Text File", "*.txt"), ("All Files", "*.*")])

            if self.__file == "":
                self.__file == None
            else:
                with open(self.__file, "w") as file_output:
                    text = self.__winTextArea.get(1.0, tk.END)
                    file_output.write(text)

                self.__root.title(f"{os.path.basename(self.__file)} | NotePad")

        else:
            with open(self.__file, "w") as file_output:
                text = self.__winTextArea.get(1.0, tk.END)
                file_output.write(text)


    def __openFIle(self):
        
        self.__file = askopenfilename(defaultextension=".txt", 
                                        filetypes=[("Text File", "*.txt"), 
                                        ("All Files", "*.*")])

        if self.__file == "":
            self.__file == None
        

        else:

            with open(self.__file, "r") as file_input:
                text = file_input.read()
                self.__winTextArea.insert(tk.END, text)
            self.__root.title(f"{os.path.basename(self.__file)} | NotePad")

    
    #EditMenu

    def __cut(self):
        self.__winTextArea.event_generate("<<Cut>>")


    def __copy(self):
        self.__winTextArea.event_generate("<<Copy>>")


    def __paste(self):
        self.__winTextArea.event_generate("<<Paste>>")


    def __counter(self):
        text = self.__winTextArea.get(1.0, tk.END)
        letter_count = 0
        
        for letter in text:
            if letter == " ":
                pass
            else:
                letter_count += 1
        word_count = text.split()

        showinfo("Text Counter | AGM", 'Letter Count: %d | Word Count: %d' % (letter_count, len(word_count))) 
 



    def run(self):
        self.__root.mainloop()

        # Run main application



pad1 = Notepad(width=600, height=400)
pad1.run()

# def saveFile():
#     file_location = asksaveasfilename(
#         initialfile="Untitled.txt",
#         defaultextension="txt",
#         filetypes=[("Text file", "*.txt"), ("All files", "*.*")]
#     )
#     if not file_location:
#         return
#     with open(file_location, "w") as file_output:
#         text = text_edit.get(1.0, tk.END)
#         file_output.write(text)

#     root.title(f"{file_location} | NotePad")


# def openFile():
#     file_location = askopenfilename(
#         filetypes=[("Text file", "*.txt"), ("All files", "*.*")]
#     )
#     if not file_location:
#         return
#     text_edit.delete(1.0, tk.END)

#     with open(file_location, "r") as file_input:
#         text = file_input.read()
#         text_edit.insert(tk.END, text)
#     root.title(f"{file_location} | NotePad")


# root = tk.Tk()

# root.title("Untitled | NotePad")

# text_edit = tk.Text(root, relief=tk.RAISED)
# text_edit.grid(row=0, column=1, sticky="nsew")

# thisMenuBar = Menu(root)

# thisFileMenu = Menu(thisMenuBar, tearoff=0)

# frame_button = tk.Frame(root, relief=tk.RAISED, bd=2)
# frame_button.grid(row=0, column=0, sticky="ns")

# button_open = tk.Button(frame_button, text="Open File", command=openFile)
# button_open.grid(row=0, column=0, padx=5, pady=5)

# button_save = tk.Button(frame_button, text="Save As", command=saveFile)
# button_save.grid(row=1, column=0, padx=5)


# root.rowconfigure(0, minsize=800)
# root.columnconfigure(1, minsize=800)


# root.mainloop()
