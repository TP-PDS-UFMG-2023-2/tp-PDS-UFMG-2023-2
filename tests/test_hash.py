from core import interfaceHash
from hash import implementacaoHash
import pytest 

from passlib.hash import pbkdf2_sha256 as sha

def test_fazHash():
    h = implementacaoHash()
    test_name = "Username"
    assert sha.verify(test_name, h.fazHash(test_name))
    test_name = "TestName"
    assert sha.verify(test_name, h.fazHash(test_name))
    test_name = "xX_EdgeL0rd_Xx"
    assert not sha.verify(test_name, h.fazHash("xX_EdgeLOrd_Xx"))
    assert sha.verify(test_name, h.fazHash(test_name))

def test_verificaHash():
    h = implementacaoHash()
    name = "User"
    hashed_name = sha.hash(name)
    assert h.verificaHash(name, hashed_name)
    name = "TestName"
    hashed_name = sha.hash(name)
    assert h.verificaHash(name, hashed_name)
    assert not h.verificaHash("WrongName", hashed_name)

