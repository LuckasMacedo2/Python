from enumLang import LanguageDestiny
from datetime import datetime

class CommentFormat:
    def __init__(self, outputLang = LanguageDestiny.none.value) -> None:
        self.name      = ""
        self.project   = ""
        self.sprint    = ""
        self.atv       = ""
    
    def assembleObject(self, strObject):
        lstStr = strObject.split('\n')
        self.name      = lstStr[0]
        self.project   = lstStr[1]
        self.sprint    = lstStr[2]
        self.atv       = lstStr[3]
    
    def disassembleObject(self):
        return f'{self.name}\n{self.project}\n{self.sprint}\n{self.atv}'

    def getComment(self, outputLang):
        separator = "'" if outputLang == LanguageDestiny.VB.value else "'''"

        return   f'{separator}Alteração  : {self.name}\t\t\tData: {datetime.now().strftime("%d/%m/%Y")}'\
               f'\n{separator}Projeto    : {self.project} - {self.sprint} - {self.atv}'\
               f'\n{separator}Manutenção :'
