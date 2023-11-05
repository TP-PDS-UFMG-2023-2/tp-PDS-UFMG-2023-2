import abc

class interfaceHash(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fazHash(self, input:str) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def verificaHash(self, input:str, hash:str) -> bool:
        raise NotImplementedError

from hash import implementacaoHash

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