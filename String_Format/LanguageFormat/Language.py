from .enumLang import LanguageDestiny
from .StringFormat import StringFormatSQL
class LanguageFactory:
    """ Objective    : Define the language
        Parameter(s) : 
        Return       :
    """  
    @staticmethod     
    def getLanguage(language, inputTxt):
        strSelect = ""
        if language == LanguageDestiny.dotNet.value:
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