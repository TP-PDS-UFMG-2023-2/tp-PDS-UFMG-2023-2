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

    # LOGIN

    def verificaLogin(self, login, senha):
        if(login == "admin" and senha == "admin"):
            #self.cadastraLogin("admin", "admin", 2)
            pass

        #listaLogins = implementacaoBD().pegaTodosLogins()
        for elemento in listaLogins:
            userID, hashLogin, hashSenha = elemento

            if(implementacaoHash().verificaHash(login, hashLogin) and 
               implementacaoHash().verificaHash(senha, hashSenha)):
                return userID
        
        return -1