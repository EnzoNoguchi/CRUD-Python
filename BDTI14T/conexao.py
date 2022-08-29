import mysql.connector #Elemento que faz a conexao como banco de dados
from mysql.connector import errorcode

class conexao:
    def __init__(self):
        pass



    def conectar(self):
        try:
            self.db_connection = mysql.connector.connect(host='localhost',
                                                         user='root',
                                                         password='',
                                                         database='bdTI14TPython')
            print('Conectado com sucesso!')
            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR: #Caso Banco de dados não exista!
                print('Banco de Dados não existe!\n Erro: {}'.format(erro))
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Há um erro de usuario!
                print('Nome de usuario ou senha invalido! \n Erro: {}'.format(erro))
            else:
                print(erro)
        else:
            self.db_connection.close() #Fechando a conexao com o banco de dados
