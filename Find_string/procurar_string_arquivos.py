"""
    Autor: Lucas Macedo da Silva
    Versão 1.1
"""
import os

def find_string(file, str, camel_case):
    """
    Procura uma string em determinado arquivo
    Parâmetros
        file: nome do arquivo em que a string será procurada
        str: a string a ser procurada
        camel_case: True se a procura pela string não ignorar maiusculas de minusculas,
                    False caso contrario
    Retorno:
        output_str: string contendo os locais em que a str aparece, da forma
                    número da linha;linha\n
    """
    output_str = ''
    try:
        line_list = open(file, 'r').readlines()
    except:
        return ";Não foi possível abrir o arquivo\n"

    for index, line in enumerate(line_list, 1):
        if line.find('\n') >=0:
            line = line[:-1]

        if camel_case:
            if line.find(str) >= 0:
                output_str += f'{index};{line}\n'
        else:
            if line.upper().find(str.upper()) >= 0:
                output_str += f'{index};{line}\n'
        
    return output_str

'''
    Procura strings em arquivos presentes em diversos diretorios
        DIR_LIST: Lista com os diretórios em que os arquivos seram procurados
        str_find_list: Lista com as strings a serem procuradas
        camel_case: True se a procura pela string não ignorar maiusculas de minusculas,
                    False caso contrario
        output_file: arquivo de saída
'''

# Lista com os diretorios a serem procurados
DIR_LIST = ['D:\\Estudos\\Eng. de Computação\\Processamento Digital de Imagens\\PCA e Classificação\\Código_Versão4.0']
# Lista com as strings a serem procuradas
str_find_list = ['imagem', 'otsu', 'subplot']
camel_case = False

output_file = open("saida.csv", "w")

for dir in DIR_LIST:
    file_list = os.listdir(dir)
    
    output_file.write('--------------;--------------\n')
    output_file.write(f'Diretório;{dir}\n')

    for file in file_list:
        
        output_file.write(f'\nArquivo;{file}\n')
        for str in str_find_list:
            output_str = ''
            output_file.write(f'Palavra chave;{str}\n')
            output_str += find_string(dir + '\\' + file, str, camel_case)

            if output_str != '' and output_str != '\n':
                output_file.write(output_str)
            else:
                output_file.write(';Não encontrada\n')

output_file.close()