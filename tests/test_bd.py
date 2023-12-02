from core import interfaceBD
from bd import implementacaoBD
import pytest

def GetUserID(impl, user, senha):
    listaLogins = impl.pegaTodosLogins()
    for element in listaLogins:
        userID, hashLogin, hashSenha = element
        if(hashLogin == user and hashSenha == senha):
            return userID
    return -1

def test_init_functions():
    impl = implementacaoBD()
    tables = impl.realizaQuery(
        """
        SELECT name FROM sqlite_master WHERE type='table'
        """
    ).values.tolist()
    tables = [x[0] for x in tables]
    assert "loginTable" in tables
    assert "courseTable" in tables
    assert "reviewTable" in tables
    assert "imageTable" in tables

def test_cadastraLogin():
    impl = implementacaoBD()
    first_cadastro = impl.cadastraLogin("Test_user", "5")
    second_cadastro = impl.cadastraLogin("Test_user", "5")

    assert first_cadastro == 0
    assert second_cadastro == -2

    impl.cursor.execute(
        """
        DELETE FROM loginTable WHERE LOGIN="Test_user" AND SENHA="5"
        """
    )
def test_Query():
    impl = implementacaoBD()
    hasException = False
    query = None
    try:
        query = impl.realizaQuery("SELECT * FROM loginTable")
    except:
        hasException = True
    assert not hasException and query is not None

def test_cadastraMatricula():
    impl = implementacaoBD()

    test_user = impl.cadastraLogin("Test_user", "5")
    id = GetUserID(impl, "Test_user", "5")
    assert id >= 0
    success = impl.cadastraMatricula(id, "6")
    assert success == 0
    mat = impl.realizaQuery(
        """
            SELECT matricula
            FROM loginTable
            WHERE userID = %d
        """%(id)
    ).values

    assert mat == "6"

    impl.cursor.execute(
        """
        DELETE FROM loginTable WHERE LOGIN="Test_user" AND SENHA="5"
        """
    )
    
def test_aceita_recusa_Usuario():
    impl = implementacaoBD()
    first_cadastro = impl.cadastraLogin("Test_user", "5")
    id = GetUserID(impl, "Test_user", "5")
    success = impl.aceitaUsuario(id)
    permLvl = impl.realizaQuery(
        """ 
        SELECT permLvl
        FROM loginTable
        WHERE userID = %d;
        """%id
    ).values
    assert success == 0
    assert permLvl == 1
    success = impl.recusaUsuario(id)
    permLvl = impl.realizaQuery(
        """ 
        SELECT permLvl
        FROM loginTable
        WHERE userID = %d;
        """%id
    ).values
    assert success == 0
    assert permLvl == -1

    impl.cursor.execute(
        """
        DELETE FROM loginTable WHERE LOGIN="Test_user" AND SENHA="5"
        """
    )

#def test_getListas():
#    impl = implementacaoBD()
