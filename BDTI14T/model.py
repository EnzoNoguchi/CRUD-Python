import mysql.connector
from conexao import conexao
from datetime import datetime


class model:
    def __init__(self):
        self.db_connection = conexao() #Abrindo a conexao com o banco de dados
        self.db_connection = self.db_connection.conectar() #Metodo que realiza a conexao com BD
        self.con = self.db_connection.cursor() #Navegação no banco de dados

    def inserir(self, nome, telefone, endereco, dataDeNascimento):
        try:
            sql = "insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('','{}', '{}', '{}', '{}')".format( nome, telefone, endereco, dataDeNascimento)
            self.con.execute(sql)
            self.db_connection.commit()#Insere o dado no banco de dados(Control + Enter)
            return "{} Linha afetada".format(self.con.rowcount)
        except Exception as erro:
            return erro




    def selecionar(self):
        try:
            sql = "select * from pessoa"
            self.con.execute(sql)
            msg = ""

            for(codigo, nome, telefone, endereco, dataDeNascimento) in self.con:
                msg = msg + "\nCódigo: {}, Nome: {}, Telefone: {}, Endereco: {}, Data de Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
                return msg
        except Exception as erro:
            return erro
