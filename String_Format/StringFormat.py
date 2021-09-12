from enumLang import LanguageDestiny
import re

class StringFormatSQL:
    def __init__(self, outputLang = LanguageDestiny.none) -> None:
        """ Objective    :  StringFormatSQL class constructor
            Parameter(s) : outputLang: output language for SQL statement
            Return       :
        """

        self.dictKeyWords = {'SELECT':'\n', 'FROM':'\n\t', 'INNER':'\n\t', 'AND':'', ' OR ':'', 'LEFT':'\n\t', 
                             'RIGHT':'\n\t', ' ON ':'\n\t\t', 'UPDATE':'\n', 'INSERT':'\n',
                             'INTO':'', 'VALUES':'\n', 'JOIN':'', 'SET':'\n', 'WHERE':'\n'}

        if outputLang == LanguageDestiny.dotNet.value:
            self.prefix = '.AppendLine("'
            self.sufix  = '");'
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
        print(lstStrInput)
        strOutput = ""
        for strInp in lstStrInput:
            print(">" + strInp + "<")
            strInp = self.removeCharToSQL(strInp)
            
            strOutput = f'{strOutput}\n{self.prefix}{strInp}{self.sufix}'
        
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
        lstPrefixSufixLang = ['.AppendLine(', ');', '"', '&', 'vbCrLf', '_']

        
        for prefixSufix in lstPrefixSufixLang:
            strSQL = self.replaceWithIgnoreCaseSensitive(strSQL, prefixSufix, '')
        
        strOutput = ""
        for line in strSQL.split('\n'):
            strOutput +=  line.rstrip() + '\n'
            print(strOutput)

        return strOutput[:-1]
