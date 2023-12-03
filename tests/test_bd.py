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

def test_cadastraMateria():
    impl = implementacaoBD()

    success = impl.cadastraMateria("DCC-001", "Test", "TTeach")
    mat = impl.realizaQuery(""" SELECT * FROM courseTable WHERE codigoUFMG="DCC-001" AND nome="Test" AND nomeProfessor="TTeach" """)
    assert success == 0 and mat is not None

    impl.cursor.execute(
        """
        DELETE FROM courseTable WHERE codigoUFMG="DCC-001" AND nome="Test" AND nomeProfessor="TTeach" 
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

# O formato das listas pode ser diferente, basta garantir que eles não quebram.
def test_getListas():
    impl = implementacaoBD()
    hasException = False
    query = None
    try:
        mat = impl.getListaMaterias()
        id = mat[0][0]
        impl.getListaReviewsMateria(id)
        impl.getUsersPendentes()
    except:
        hasException = True
    assert not hasException 

def test_cadastraReview():
    impl = implementacaoBD()
    mat = impl.realizaQuery(""" SELECT * FROM courseTable """).values.tolist()
    mat_id = mat[0][0]
    user_id = impl.realizaQuery(""" SELECT userID FROM loginTable LIMIT 1 """).values
    impl.cadastraReview(user_id, mat_id, 1, "TextA")
    review = impl.realizaQuery(""" SELECT * FROM reviewTable WHERE (usuario = %d AND materia = %d) """%(user_id, mat_id)).values
    assert review[0][3] == 1
    assert review[0][4] == "TextA"

    impl.cadastraReview(user_id, mat_id, 1, "TextB")
    review = impl.realizaQuery(""" SELECT * FROM reviewTable WHERE (usuario = %d AND materia = %d) """%(user_id, mat_id)).values
    assert review[0][3] == 1
    assert review[0][4] == "TextB"

    impl.cursor.execute(
        """
        DELETE FROM reviewTable WHERE (usuario = %d AND materia = %d)
        """%(user_id, mat_id)
    )

def test_CadastraGetImagem():
    impl = implementacaoBD()
    first_cadastro = impl.cadastraLogin("Test_user", "5")
    id = GetUserID(impl, "Test_user", "5")

    success = impl.cadastraImagem(id, "Img", 8)
    image_id = impl.getImagemID("Img", 8)[0]
    
    result = impl.realizaQuery(""" SELECT imageName, imageBinary FROM imageTable WHERE imageName="%s" AND imageBinary=%d; """%("Img", 8)).values[0]
    assert success >= 0 and result[0] == "Img" and result[1] == 8

    success = impl.cadastraImagem(id, "Img2", 10)
    image_id2 = impl.getImagemID("Img2", 10)[0]
    
    result = impl.realizaQuery(""" SELECT imageName, imageBinary FROM imageTable WHERE imageName="%s" AND imageBinary=%d; """%("Img2", 10)).values[0]
    assert success >= 0 and result[0] == "Img2" and result[1] == 10

    #impl.deletaImagem(image_id) Tests the case of the image existing! Don't delete!
    impl.deletaImagem(image_id2)

    success = impl.cadastraImagem(id, "Img2", 10)
    image_id2 = impl.getImagemID("Img2", 10)[0]
    
    result = impl.realizaQuery(""" SELECT imageName, imageBinary FROM imageTable WHERE imageName="%s" AND imageBinary=%d; """%("Img2", 10)).values[0]

    impl.deletaImagemUsuario(id) #Tests if this also deletes the image.

    result = impl.realizaQuery(""" SELECT imageName, imageBinary FROM imageTable WHERE imageName="%s" AND imageBinary=%d; """%("Img2", 10)).values

    assert result.tolist() == []
    
    impl.cursor.execute(
        """
        DELETE FROM loginTable WHERE LOGIN="Test_user" AND SENHA="5"
        """
    )
