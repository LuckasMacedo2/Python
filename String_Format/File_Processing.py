from enumLang import LanguageDestiny
from StringFormat import StringFormatSQL
import os

class FileProcessing:
    def __init__(self, inputFile = "", outputFile = "", inputExpression = "", separator = " ", outputLang = LanguageDestiny.none.value):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.inputExpression = inputExpression
        self.separator = separator
        self.outputLang = outputLang
    
    def openFile(self):
        linesList = []
        with open(self.inputFile, 'r') as f:
            linesList = f.readlines()
            f.close()
        return linesList
    
    def saveFile(self, strSave):
        with open(self.outputFile, 'w') as f:
            f.write(strSave)
            f.close()
        
    def fileProcess(self):
        strOuput = ""
        strTemp = ""
        strFormat = StringFormatSQL(self.outputLang)

        for line in self.openFile():
            itens = line.replace('\n', '').split(self.separator)
            strTemp = strFormat.formatSQL(self.inputExpression.format(itens[0], itens[1]))

            if self.outputLang != LanguageDestiny.none.value:
                strTemp = strFormat.formatStringToOutputLang(strTemp)

            strOuput = f'{strOuput}{strTemp}\n\n'

        
        self.saveFile(strOuput)

fileProcessing = FileProcessing(f'{os.getcwd()}\\Files\\teste.txt', 
                                f'{os.getcwd()}\\Files\\outputFile.txt', 
                                "Update teste teste set asd = {1} ANd st = {0} where {0} = {1}", 
                                " ",
                                LanguageDestiny.VB.value)
                                
fileProcessing.fileProcess()

