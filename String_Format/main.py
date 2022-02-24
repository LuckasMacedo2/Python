from LanguageFormat.Language import LanguageFactory
from MockData.MockUtils import MockUtils
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import pyperclip

"""
Developer: Lucas Macedo da Silva

Project: SQL formatter

Objective: Facilitate formatting of SQL statements

Usage: Install python 3.7 and the pyperclip library
"""

def submitFunction(event = None):
    """ Objective    : Callback function for occurrence of language choice event in combobox
        Parameter(s) : 
        Return       :
    """  
    inputTxt = txt.get(1.0, "end-1c")
    inputOpc = cboOpc.current()

    if inputTxt == "":
        messagebox.showinfo(title='Info', message='Please inform the instruction')
    else:
        clear()
        txt.insert(INSERT, LanguageFactory.getLanguage(inputOpc, inputTxt))
        

def clear():
    """ Objective    : Clear the textbox
        Parameter(s) : 
        Return       :
    """  
    txt.delete(1.0, END)

def copy():
    """ Objective    : Copy the textbox content
        Parameter(s) : 
        Return       :
    """  
    inputTxt = txt.get(1.0, "end-1c")
    if inputTxt != "":
        pyperclip.copy(inputTxt)

def generateMockData():
    """ Objective    : Generate mock data
        Parameter(s) : 
        Return       :
    """  
    inputTxt = txtNumberOfCaracter.get(1.0, "end-1c")
    if inputTxt == "":
        messagebox.showinfo(title='Info', message='Please inform the length of data')
    else:
        clear()
        txt.insert(INSERT, MockUtils.generateMockData(int(inputTxt)))

def calculateDataLength():
    """ Objective    : Calculate data length
        Parameter(s) : 
        Return       :
    """  
    txtDataLength.delete(1.0, END)
    inputTxt = txt.get(1.0, "end-1c")
    if inputTxt == "":
        messagebox.showinfo(title='Info', message='Please inform the data')
    else:
        txtDataLength.insert(INSERT, MockUtils.dataLength(inputTxt))


m = Tk()
m.title('Utils')

separator1 = ttk.Separator(m, orient=VERTICAL)
separator1.place(x=0, y = 100, relwidth=1)



lblSQL = Label(m, text='SQL Utils:')
lblSQL.place(x=10, y=5)

lblSQLOptions = Label(m, text='Select option:')
lblSQLOptions.place(x=10, y=30)


cboOpc = ttk.Combobox(m, values = ['', '.Net', 'VB6', 'Upper SQL', 'Format SQL', 'Clear SQL'], width=30)
cboOpc.bind('<<ComboboxSelected>>', submitFunction)
cboOpc.place(x=100, y=30)
btnExecute = Button(m, text='Execute', command=submitFunction, width=10)
btnExecute.place(x=320, y=30)

lblStr = Label(m, text='String Utils:')
lblStr.place(x=430, y=5)

lblStrNumber = Label(m, text='Number of caracteres:')
lblStrNumber.place(x=430, y=30)
txtNumberOfCaracter = Text(m, width=15, height=0)
txtNumberOfCaracter.place(x = 560, y = 30)
txtNumberOfCaracter['font'] = ('times', '12')
btnGenerateMock = Button(m, text='Generate', command=generateMockData, width=15)
btnGenerateMock.place(x=690, y=25)

lblStrData = Label(m, text='Data length:')
lblStrData.place(x=430, y=70)
btnCalculateDataLength = Button(m, text='Calculate', command=calculateDataLength, width=15)
btnCalculateDataLength.place(x=560, y=70)
txtDataLength = Text(m, width=15, height=0)
txtDataLength.place(x = 690, y=70)
txtDataLength['font'] = ('times', '12')

btnClear = Button(m, text='Clear', command=clear, width=25)
btnClear.place(x=10, y=110)

btnCopy = Button(m, text='Copy', command=copy, width=25)
btnCopy.place(x=220, y=110)

lblStr = Label(m, text='Data:')
lblStr.place(x=10, y=150)

txt = scrolledtext.ScrolledText(m, undo=True)
txt['font'] = ('times', '12')
txt.pack(padx=10, pady=170, expand=True, fill='both')



m.mainloop()
