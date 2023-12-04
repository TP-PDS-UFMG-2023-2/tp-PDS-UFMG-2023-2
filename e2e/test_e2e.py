import time
import os
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestEnd2End:
    def setup_class(self):
        options = ChromiumOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def teardown_class(self):
        self.driver.quit()

    def teardown_method(self):
        self.logout()

    def test_admin_login(self):
        # Eu, como gerente do sistema, gostaria de ter um login único e com privilegios maiores
        self.loginAdmin()

        self.driver.find_element(By.LINK_TEXT, "[Admin] Validar usuário").click()
        time.sleep(1)

        label = self.driver.find_element(By.TAG_NAME, "label")

        assert label.is_displayed()

    def test_admin_aprova_user(self):
        # Eu, como gerente do sistema, gostaria de aceitar ou recusar o registro de um aluno
        user = self.randomStr(10)
        senha = self.randomStr(10)
        mat = self.randomStr(8, string.digits)

        self.cadastraUser(user, senha, mat)
        self.loginAdmin()

        self.driver.find_element(By.LINK_TEXT, "[Admin] Validar usuário").click()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "div[data-baseweb='select']").click()
        time.sleep(1)
        submissions = self.driver.find_elements(By.CSS_SELECTOR, "li[role='option']")
        submissions[-1].click()
        time.sleep(1)

        self.driver.find_elements(By.CSS_SELECTOR, "button[data-testid='baseButton-secondary']")[0].click()
        self.logout()
    
        # Eu, como aluno e usuário, gostaria de logar no sistema se minha conta for aceita ou ter um aviso que ela está pendente ou recusada
        self.login(user, senha)

        self.driver.find_element(By.LINK_TEXT, "Meu perfil").click()
        time.sleep(1)

        nome, matricula, statusPerfil, foto = self.driver.find_elements(By.CSS_SELECTOR, "p")

        assert statusPerfil.text.endswith("Aprovado!")


    def test_cadastra_aluno(self):
        # Eu, como aluno e usuário, gostaria de criar uma conta no sistema
        # Eu, como aluno e usuário, gostaria de poder colocar a foto da minha carteira no sistema para ser validada (e como gerente ver essa imagem)
        user = self.randomStr(10)
        senha = self.randomStr(10)
        mat = self.randomStr(8, string.digits)

        self.cadastraUser(user, senha, mat)
        self.login(user, senha)
        
        self.driver.find_element(By.LINK_TEXT, "Meu perfil").click()
        time.sleep(1)

        nome, matricula, statusPerfil, foto = self.driver.find_elements(By.CSS_SELECTOR, "p")

        assert nome.text.endswith(user)

    # Eu, como gerente do sistema, gostaria de adicionar disciplinas a serem avaliadas
    # Eu, como aluno e usuário, gostaria de votar em uma disciplina com a possibilidade de um comentário opcional
    # Eu, como aluno e usuário, gostaria de pesquisar dentre as disciplinas existentes no sistema e ver seus reviews

    def loginAdmin(self):
        self.login("admin", "admin")

    def cadastraUser(self, nome, senha, matricula):
        self.driver.get("http://127.0.0.1:8501/Cadastro")
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Matrícula']")\
            .send_keys(matricula, Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Usuário']")\
            .send_keys(nome, Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Senha']")\
            .send_keys(senha, Keys.ENTER)
        
        upload_file = "/temp/carteirinha.png"
        file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(os.getcwd() + upload_file)
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='baseButton-secondaryFormSubmit']").click()
        time.sleep(1)

    def login(self, user, password):
        self.driver.get("http://127.0.0.1:8501/Login")
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")\
            .send_keys(user, Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")\
            .send_keys(password, Keys.ENTER)

        self.driver.find_element(By.CSS_SELECTOR, "button[kind='secondary']").click()
        time.sleep(2)
    
    def logout(self):
        self.driver.get("http://127.0.0.1:8501")

    def randomStr(self, n, letters = string.ascii_letters + string.digits + string.punctuation + string.whitespace):
        return ''.join(random.choice(letters) for i in range (n))

    


if __name__ == "__main__":
    options = ChromiumOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--headless")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://127.0.0.1:8501/Login")
    time.sleep(2)

    inputs = driver.find_elements(By.CSS_SELECTOR, ".st-bd .st-by")
    for inp in inputs:
        print(inp.accessible_name)
    driver.quit()