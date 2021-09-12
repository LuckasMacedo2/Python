from enumLang import LanguageDestiny
from StringFormat import StringFormatSQL
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import pyperclip

"""
Developer: Lucas Macedo da Silva

Project: SQL formatter

Objective: Facilitate formatting of SQL statements

Usage: Install python 3.7 and the pyperclip library
"""

def readFile(strFile):
    """ Objective    : read the input file
        Parameter(s) : strFile: input file name
        Return       : lstStrRead: list with the lines of the file
    """                
    with open(strFile, 'r') as file:
        lstStrRead = file.read().splitlines()
        file.close()
    
    return lstStrRead

def writeFile(strFile, strWrite):
    """ Objective    : write file
        Parameter(s) : strFile: file name to be saved
                       strWrite: string to be saved
        Return       : 
    """                
    with open(strFile, 'w') as file:
        file.write(strWrite)
        file.close()

def submitFunction():
    inputTxt = txt.get(1.0, "end-1c")
    
    inputOpc = opc.get()

    if inputTxt == "":
        messagebox.showinfo(title='Info', message='Please inform the instruction')
    else:
        if inputOpc == LanguageDestiny.dotNet.value:
            strFormat = StringFormatSQL(LanguageDestiny.dotNet.value)
            clear()
            txt.insert(INSERT, strFormat.formatStringToOutputLang(inputTxt))

        elif inputOpc == LanguageDestiny.VB.value:
            strFormat = StringFormatSQL(LanguageDestiny.VB.value)
            clear()
            txt.insert(INSERT, strFormat.formatStringToOutputLang(inputTxt))
        
        elif inputOpc == LanguageDestiny.upperSQL.value:
            strFormat = StringFormatSQL(LanguageDestiny.upperSQL.value)
            clear()
            txt.insert(INSERT, strFormat.upperSQL(inputTxt))
        
        elif inputOpc == LanguageDestiny.formatSQL.value:
            strFormat = StringFormatSQL(LanguageDestiny.formatSQL.value)
            clear()
            txt.insert(INSERT, strFormat.formatSQL(inputTxt))
        
        elif inputOpc == LanguageDestiny.clearLang.value:
            strFormat = StringFormatSQL(LanguageDestiny.clearLang.value)
            clear()
            txt.insert(INSERT, strFormat.removeCharToSQL(inputTxt))
        

def clear():
    txt.delete(1.0, END)

def copy():
    inputTxt = txt.get(1.0, "end-1c")
    if inputTxt != "":
        pyperclip.copy(inputTxt)

m = Tk()
m.title('SQL formatter')

Label(m, text='Select option:').pack(anchor=W)


opc = IntVar()
Radiobutton(m, text='.Net', variable=opc, value=int(LanguageDestiny.dotNet.value), command=submitFunction).pack(anchor=W)
Radiobutton(m, text='VB6', variable=opc, value=int(LanguageDestiny.VB.value), command=submitFunction).pack(anchor=W)
Radiobutton(m, text='Upper SQL', variable=opc, value=int(LanguageDestiny.upperSQL.value), command=submitFunction).pack(anchor=W)
Radiobutton(m, text='Format SQL', variable=opc, value=int(LanguageDestiny.formatSQL.value), command=submitFunction).pack(anchor=W)
Radiobutton(m, text='Clear SQL', variable=opc, value=int(LanguageDestiny.clearLang.value), command=submitFunction).pack(anchor=W)

Button(m, text='Clear', command=clear).pack(anchor=CENTER)
Button(m, text='Copy', command=copy).pack(anchor=CENTER)

txt = scrolledtext.ScrolledText(m, undo=True)
txt['font'] = ('times', '12')
txt.pack(expand=True, fill='both')

m.mainloop()