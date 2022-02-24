import sys
from enum import Enum
import re

class StringFormatSQL:
    def __init__(self, outputLang = LanguageDestiny.none.value) -> None:
        """ Objective    : StringFormatSQL class constructor
            Parameter(s) : outputLang: output language for SQL statement
            Return       :
        """

        self.dictKeyWords = {'SELECT':'', 'FROM':'\n       ', 'INNER':'\n ', 'AND':'\n\t\t', ' OR ':'', 'LEFT':'\n  ', 
                             'RIGHT':'\n\t', ' ON ':'\n\t\t', 'UPDATE':'\n', 'INSERT':'\n',
                             'INTO':'', 'VALUES':'\n', 'JOIN':'', 'SET':'\n', 'WHERE':'\n', 'ORDER BY':'\n',
                             'NOT':'', 'NULL':'', ' DESC ':'', ' ASC ':'', ' IN ':'', ' IS ':'', ',':'\n       '}

        if outputLang == LanguageDestiny.dotNet.value:
            self.prefix = '.AppendLine("'
            self.sufix  = '")'
        elif outputLang == LanguageDestiny.VB.value:
            self.prefix = '"'
            self.sufix  = '" & vbCrLf & _'
        else:
            self.prefix = ''
            self.sufix  = ''
    
    def formatStringToOutputLang(self, strInput):
        """ Objective    : format the instruction to the language for the output
            Parameter(s) : strInput: string with the instruction separated by lines
            Return       : strOutput: string with formatted instruction
        """  
        lstStrInput = strInput.split('\n')
        strOutput = ""
        for strInp in lstStrInput:
            strInp = self.removeCharToSQL(strInp)
             
            strOutput = f'{strOutput}\n{self.prefix}{strInp}{self.sufix}'

        if self.sufix  == '" & vbCrLf & _':
            strOutput = strOutput[:len(strOutput)-len('" & vbCrLf & _')+1]
        
        return strOutput[1:]

    def upperSQL(self, strSQL):
        """ Objective    : Remove characters from SQL statement
            Parameter(s) : strSQL: SQL statement
            Return       : strOutput: Upper SQL statement
        """                
        for keyWord in self.dictKeyWords.keys():
            strSQL = self.replaceWithIgnoreCaseSensitive(strSQL, keyWord, keyWord)

        return strSQL
    
    def formatSQL(self, strSQL):
        """ Objective    : Format the SQL statement with line breaks and tabs
            Parameter(s) : strSQL: SQL statement
            Return       : strSQL: SQL statement formatted
        """                
        strSQL = ' '.join(strSQL.replace('\t', ' ').replace('\n', ' ').split())

        for keyWord in self.dictKeyWords.keys():
            strSQL = self.replaceWithIgnoreCaseSensitive(strSQL, keyWord, f'{self.dictKeyWords[keyWord]}{keyWord}')

        if strSQL[0] == '\n':
            strSQL = strSQL[1:]

        return strSQL
    
    def replaceWithIgnoreCaseSensitive(self, strInput, strReplace, strNewValue):
        """ Objective    : Remove characters and ignore case sensitive
            Parameter(s) : strInput: String with the expression to be ignored
                           strReplace: String with the characters to be ignored
                           strNewValue: New value
            Return       : obj temp: String with the characters replaced
        """ 
        varRe = re.compile(re.escape(strReplace), re.IGNORECASE)
        return varRe.sub(strNewValue, strInput)
    
    def removeCharToSQL(self, strSQL):
        """ Objective    : Remove characters from SQL statement
            Parameter(s) : strSQL: SQL statement
            Return       : strOutput: Clear SQL statement
        """ 
        lstPrefixSufixLang = ['.AppendLine(', '")', '"', '& vbCrLf & _', '& _', '$', '"', 'strS', '& vbCrLf']

        
        for prefixSufix in lstPrefixSufixLang:
            strSQL = self.replaceWithIgnoreCaseSensitive(strSQL, prefixSufix, '')
        
        strOutput = ""
        for line in strSQL.split('\n'):
            strOutput +=  line.rstrip() + '\n'

        return strOutput[:-1]

class LanguageDestiny(Enum):
    """ Objective    : Enum class representing output languages
        Parameter(s) : 
        Return       :
    """       
    none        = 0          
    dotNet      = 1
    VB          = 2
    upperSQL    = 3
    formatSQL   = 4
    clearLang   = 5
        


class LanguageFactory:
    """ Objective    : Define the language
        Parameter(s) : 
        Return       :
    """  
    @staticmethod     
    def getLanguage(language, inputTxt):
        strSelect = ""
        if language == Lan
            strFormat = StringFormatSQL(LanguageDestiny.dotNet.value)
            strSelect = strFormat.formatStringToOutputLang(inputTxt)
        elif language == LanguageDestiny.VB.value:
            strFormat = StringFormatSQL(LanguageDestiny.VB.value)
            strSelect = strFormat.formatStringToOutputLang(inputTxt)
        elif language == LanguageDestiny.upperSQL.value:
            strFormat = StringFormatSQL(LanguageDestiny.upperSQL.value)
            strSelect = strFormat.upperSQL(inputTxt)
        elif language == LanguageDestiny.formatSQL.value:
            strFormat = StringFormatSQL(LanguageDestiny.formatSQL.value)
            strSelect = strFormat.formatSQL(inputTxt)
        elif language == LanguageDestiny.clearLang.value:
            strFormat = StringFormatSQL(LanguageDestiny.clearLang.value)
            strSelect = strFormat.removeCharToSQL(inputTxt)

        return strSelect
        