import sqlite3
import pandas as pd
from PIL import Image

from core import interfaceBD

class implementacaoBD(interfaceBD):

    def __init__(self):
        self.conn = sqlite3.connect("./database.db")
        self.cursor = self.conn.cursor()
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.verificarTabelaLogins()
        self.verificarTabelaMaterias()
        self.verificarTabelaReviews()
        self.verificarTabelaImagens()
    
    def __del__(self):
        self.close()

    def close(self):
        self.commit()
        self.cursor.close()
        self.conn.close()

    def verificarTabelaLogins(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS loginTable(
                userID INTEGER PRIMARY KEY,
                login VARCHAR(255),
                senha VARCHAR(255),
                permLvl INTEGER,
                imagem INTEGER,
                matricula VARCHAR(255),
                FOREIGN KEY(imagem) REFERENCES imageTable(imageID) ON DELETE SET NULL,
                UNIQUE(login, senha)
            );
            """)   
    def verificarTabelaMaterias(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS courseTable(
                materiaID INTEGER PRIMARY KEY,
                codigoUFMG VARCHAR(255),
                nome VARCHAR(255),
                nomeProfessor VARCHAR(255),
                UNIQUE(codigoUFMG, nomeProfessor)
            )
            """)
    def verificarTabelaReviews(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS reviewTable(
                reviewID INTEGER PRIMARY KEY,
                usuario INTEGER,
                materia INTEGER,
                nota INTEGER,
                review VARCHAR(255),
                FOREIGN KEY(usuario) REFERENCES loginTable(userID) ON DELETE CASCADE,
                FOREIGN KEY(materia) REFERENCES courseTable(materiaID) ON DELETE CASCADE
            )
            """)
    def verificarTabelaImagens(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS imageTable(
                imageID INTEGER PRIMARY KEY,
                imageName VARCHAR(255),
                imageBinary BLOB
            )
            """)
    
    def realizaQuery(self, query):
        return pd.read_sql_query(query, self.conn)
    def commit(self):
        self.conn.commit()

    def cadastraLogin(self, login, senha, permLvl=0):
        """
        Retorna  0 se inseriu com sucesso
        Retorna -1 se ocorreu um erro desconhecido
        Retorna -2 se o usuário já está cadastrado
        """

        lista = self.realizaQuery("""
            SELECT login, count(*) as C
            FROM loginTable
            WHERE LOGIN = \"%s\"
            GROUP BY login
        """%(login))["C"]

        if (len(lista) != 0):
            return -2 # usuário já existe no banco de dados


        try:
            self.cursor.execute(
                """
                INSERT INTO loginTable(login, senha, permLvl) VALUES ("%s", "%s", %d);
                """%(login, senha, permLvl))
        except Exception as e:
            print(e)
            return -1
        return 0    
    def cadastraMatricula(self, usuario, matricula):
        try:
            self.cursor.execute("""
                UPDATE loginTable
                SET matricula = "%s"
                WHERE userID = %d
            """%(matricula, usuario))
        except Exception as e:
            print(e)
            return -1
        return 0
    def pegaTodosLogins(self):
        """
        Retorna todos os ids / hash de login / hash de senha
        """
        lista = self.realizaQuery(
            """
            SELECT userID, login, senha
            FROM loginTable
            """).values.tolist()
        return lista

    def aceitaUsuario(self, userID):
        try:
            self.cursor.execute(
                """
                UPDATE loginTable
                SET permLvl = 1
                WHERE userID = %d;
                """%userID)
        except Exception as e:
            print(e)
            return -1
        return 0   
    def recusaUsuario(self, userID):
        try:
            self.cursor.execute(
                """
                UPDATE loginTable
                SET permLvl = -1
                WHERE userID = %d;
                """%userID)
        except Exception as e:
            print(e)
            return -1
        return 0   

    def getListaMaterias(self):
        """
        Retorna lista de listas (python)
        Contém ID das matérias, código UFMG, nome da matéria e nome do professor, nessa ordem
        """

        return self.realizaQuery("""
            SELECT *
            FROM courseTable
        """).values.tolist()
    def getListaReviewsMateria(self, materia):
        """
        Retorna lista de listas (python)
        Contém reviewID, usuarioID, materiaID, nota, mensagem, nessa ordem
        """
        return self.realizaQuery("""
            SELECT *
            FROM reviewTable
            WHERE materia = %d
        """%(materia)).values.tolist()

    def cadastraReview(self, usuario, materia, nota, review=""):
        try:
            lista = self.realizaQuery(
            """
            SELECT reviewID
            FROM reviewTable
            WHERE (usuario = %d AND materia = %d)
            """%(usuario, materia))["reviewID"].to_list()

            if(len(lista) != 0):
                self.cursor.execute("""
                    DELETE FROM reviewTable
                    WHERE (usuario = %d AND materia = %d)
                """%(usuario, materia))

            self.cursor.execute(
                """
                INSERT INTO reviewTable(usuario, materia, nota, review) VALUES (%d, %d, %d, "%s");
                """%(usuario, materia, nota, review))
        except Exception as e:
            print(e)
            return -1
        return 0
    def cadastraMateria(self, codigoUFMG, nome, nomeProfessor):
        try:
            self.cursor.execute(
                """
                INSERT INTO courseTable(codigoUFMG, nome, nomeProfessor) VALUES ("%s", "%s", "%s");
                """%(codigoUFMG, nome, nomeProfessor))
        except Exception as e:
            print(e)
            return -1
        return 0
    def cadastraImagem(self, usuario, imageName, imageBinary):
        try:
            # caso da imagem já estar cadastrada
            listaPreemptiva = self.getImagemID(imageName, imageBinary)
            if(len(listaPreemptiva)!=0):
                idImagem = listaPreemptiva[0]
                self.cursor.execute(
                """
                UPDATE loginTable
                SET imagem = %d
                WHERE userID = %d
                """%(idImagem, usuario))
                return idImagem

            # cadastra imagem
            tupla = (imageName, imageBinary)
            self.cursor.execute(
                """
                INSERT INTO imageTable(imageName, imageBinary) VALUES (?, ?);
                """, tupla)

            listaID = self.getImagemID(imageName, imageBinary)
            if(len(listaID) == 0):
                return -1
            
            idImagem = listaID[0]
            
            self.cursor.execute(
                """
                UPDATE loginTable
                SET imagem = %d
                WHERE userID = %d
                """%(idImagem, usuario))

        except Exception as e:
            print(e)
            return -1
        return idImagem
    def getImagemID(self, imageName, imageBinary):
        """
        Retorna lista contendo todos os IDs de imagens, com aquele nome e aquele binary
        """
        try:
            tupla = (imageName, imageBinary)

            self.cursor.execute(
                """
                SELECT imageID
                FROM imageTable
                WHERE (imageName, imageBinary) = (?, ?);
                """, tupla)
            lista = pd.DataFrame(self.cursor.fetchall(), columns=["ImageID"])["ImageID"].to_list()
        except Exception as e:
            print(e)
            return lista
        return lista
    def deletaImagem(self, imageID):
        try:
            self.cursor.execute(
                """
                DELETE FROM imageTable 
                WHERE imageID = %d;
                """%imageID)
        except Exception as e:
            print(e)
            return -1
        return 0
    def deletaImagemUsuario(self, usuario):
        try:
            
            lista = self.realizaQuery("""
            SELECT imagem
            FROM loginTable
            WHERE userID = %d
            """%usuario)["imagem"].to_list()


            for imageID in lista:
                if imageID != None:
                    self.deletaImagem(imageID)


        except Exception as e:
            print(e)
            return -1
        
        return 0
    def salvaImagemUsuario(self, usuario, filename):
        """
        Retorna  0 para sucesso
        Retorna -1 para erro desconhecido
        Retorna -2 para usuário não encontrado
        Retorna -3 para usuário sem foto
        """

        try:
            listaImagem = self.realizaQuery("""
            SELECT imagem
            FROM loginTable
            WHERE userID = %d
            """%usuario)["imagem"].to_list()

            if(len(listaImagem) == 0): # não achou o usuário
                return -2
            
            imagemID = listaImagem[0]
            if(imagemID == None): # usuário não tem imagem
                return -3
            
            binario = self.realizaQuery("""
            SELECT imageBinary
            FROM imageTable
            WHERE imageID = %d
            """%imagemID)["imageBinary"].to_list()[0]

            with open(filename, "wb") as file:
                file.write(binario)


            return 0
        except Exception as e:
            print(e)
            return -1
        
        return 0

    def retornaReviewUsuario(self, usuario, materia):
        """
        Retorna uma lista python contendo usuario (id), matéria (id), a nota dada e a review, nessa ordem
        """
        lista = self.realizaQuery("""
        SELECT usuario, materia, nota, review
        FROM reviewTable
        WHERE usuario = %d AND materia = %d 
        """%(usuario, materia)).values.tolist()

        return lista
    def retornaInfosUsuario(self, usuario):
        x = self.realizaQuery("""
        SELECT userID, permLvl, matricula
        FROM loginTable
        WHERE userID = %d
        """%usuario).values.tolist()[0]
        return x


    def removeMateria(self, materia):
        try:
            self.cursor.execute(
                """
                DELETE FROM courseTable
                WHERE materiaID = %d
                """%materia)
        except Exception as e:
            print(e)
            return -1
        return 0

    def getUsersPendentes(self):
        x = self.realizaQuery("""
        SELECT userID, matricula, imagem
        FROM loginTable
        WHERE permLvl = 0
        """).values.tolist()
        return x

