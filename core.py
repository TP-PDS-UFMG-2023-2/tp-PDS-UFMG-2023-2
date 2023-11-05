import abc

class interfaceHash(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fazHash(self, input:str) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def verificaHash(self, input:str, hash:str) -> bool:
        raise NotImplementedError

class interfaceBD(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cadastraLogin(self, login, senha, permLvl=0):
        raise NotImplementedError
    
    @abc.abstractmethod
    def pegaTodosLogins(self):
        raise NotImplementedError

    @abc.abstractmethod
    def cadastraReview(self, usuario, nota, review):
        raise NotImplementedError
    
    @abc.abstractmethod
    def cadastraMateria(self, codigoUFMG, nome, nomeProfessor):
        raise NotImplementedError
    
    @abc.abstractmethod
    def aceitaUsuario(self, userID):
        raise NotImplementedError

    @abc.abstractmethod    
    def recusaUsuario(self, userID):
        raise NotImplementedError
    
    @abc.abstractmethod
    def getListaMaterias(self):
        raise NotImplementedError

    @abc.abstractmethod
    def getListaReviewsMateria(self, materia):
        raise NotImplementedError

    @abc.abstractmethod
    def cadastraReview(self, usuario, materia, nota, review=""):
        raise NotImplementedError

    @abc.abstractmethod
    def cadastraMateria(self, codigoUFMG, nome, nomeProfessor):
        raise NotImplementedError

    @abc.abstractmethod
    def removeMateria(self, materia):
        raise NotImplementedError
    
    def getUsersPendentes(self):
        raise NotImplementedError

from hash import implementacaoHash
from bd import implementacaoBD


class interfaceFrontEnd:


    # CADASTRO

    def cadastraLogin(self, login, senha, permLvl, matricula=""):
        """
        Retorna  0 se inseriu com sucesso
        Retorna -1 se ocorreu um erro desconhecido
        Retorna -2 se o usuário já está cadastrado
        Retorna -3 se houve algum erro no cadastro da matrícula
        """

        listaLogins = implementacaoBD().pegaTodosLogins()
        for elemento in listaLogins:
            userID, hashLogin, hashSenha = elemento
            if(implementacaoHash().verificaHash(login, hashLogin)): # se o login já tiver cadastrado
                return -2
        returnCadastro = implementacaoBD().cadastraLogin(implementacaoHash().fazHash(login),
                                               implementacaoHash().fazHash(senha),
                                               permLvl)
        
        id = self.verificaLogin(login, senha)
        if(id == -1):
            return -1

        returnMatricula = implementacaoBD().cadastraMatricula(id, matricula)

        if(returnMatricula == -1):
            return -3
        else:
            return returnCadastro


    # LOGIN

    def verificaLogin(self, login, senha):
        if(login == "admin" and senha == "admin"):
            self.cadastraLogin("admin", "admin", 2)

        listaLogins = implementacaoBD().pegaTodosLogins()
        for elemento in listaLogins:
            userID, hashLogin, hashSenha = elemento

            if(implementacaoHash().verificaHash(login, hashLogin) and 
               implementacaoHash().verificaHash(senha, hashSenha)):
                return userID
        
        return -1

    # VALIDAR USUARIO

    def aceitaUsuario(self, usuario):
        return implementacaoBD().aceitaUsuario(usuario)

    def recusaUsuario(self, usuario):
        return implementacaoBD().recusaUsuario(usuario)

    # MATERIAS

    def getListaMaterias(self):
        return implementacaoBD().getListaMaterias()
    
    def getReviewMateria(self, materia):
        return implementacaoBD().getListaReviewsMateria(materia)

    # FAZER REVIEW

    def cadastraReview(self, usuario, materia, nota, review):
        return implementacaoBD().cadastraReview(usuario, materia, nota, review)

    def retornaReviewUsuario(self, usuario, materia):
        return implementacaoBD().retornaReviewUsuario(usuario, materia)

    # CRIAR REMOVER MATERIAS

    def cadastraMateria(self, codigoUFMG, nome, nomeProfessor):
        return implementacaoBD().cadastraMateria(codigoUFMG, nome, nomeProfessor)

    def removeMateria(self, materia):
        return implementacaoBD().removeMateria(materia)

    # DESORGANIZADO

    
    def retornaInfosUsuario(self, usuario):
        return implementacaoBD().retornaInfosUsuario(usuario)
    
    def getUsersPendentes(self):
        return implementacaoBD().getUsersPendentes()
