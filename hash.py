from core import interfaceHash

from passlib.hash import pbkdf2_sha256 as sha

class implementacaoHash(interfaceHash):
    def fazHash(self, input:str) -> str:
        return sha.hash(input)
    
    def verificaHash(self, input:str, hash:str) -> bool:
        return sha.verify(input, hash)