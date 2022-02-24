from sys import argv
from LanguageFormat.Language import LanguageFactory
from MockData.MockUtils import MockUtils

if __name__ == '__main__':
    functionName = argv[1]
    functionArgs = argv[2]

    txt = "Não encontrado!"

    if functionName == "getLanguage":
        inputOpc, inputTxt = argv[2].split(';')
        txt = LanguageFactory.getLanguage(int(inputOpc), inputTxt)

    print(txt)