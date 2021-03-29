
from selenium import webdriver

import time


class TimControleFluxoPos:
    def __init__(self):
        self.link = 'https://contratecontrole.tim.com.br/?sku=TCPE027SP_MIGRACAO&uf=SP'
        self.name = 'Juquinha Pai'
        self.cpf = '04888673209'
        self.mae = 'Juquinha Mãe'
        self.telefone = '21999999999'
        self.dataNascimento = '17012000'
        self.numeroCasa = '1240'
        self.cep = '21250450'
        self.sms = '9997'
        self.email = 'aline.wooza@wooza.com.br'
        self.driver = webdriver.Chrome('./chromedriver.exe')

    def entrarModal(self):
        driver = self.driver
        driver.get(self.link)

    def escolherPlano(self):
        button = self.driver.find_element_by_class_name('wEnGX')
        button.click()

    def NextStep2(self):
        button = self.driver.find_element_by_xpath(
            "//button[@type='button']")
        button.click()

    def NextStep3(self):
        button = self.driver.find_element_by_xpath(
            "//button[@id='formNewUserSubmit']")
        button.click()

    def NextStep4(self):
        button = self.driver.find_element_by_xpath(
            "//input[@type='button']")
        button.click()

    def NextSubmit(self):
        button = self.driver.find_element_by_xpath("//button[@type='submit']")
        button.click()

    # @staticmethod
    def preencherDados(self):
        time.sleep(3)

        # Email
        emailInput = self.driver.find_element_by_xpath(
            "//input[@type='email']")
        emailInput.clear()
        emailInput.send_keys(self.email)

        # Phone
        phoneInput = self.driver.find_element_by_xpath(
            "//input[@name='linha']")
        phoneInput.clear()
        phoneInput.send_keys(self.telefone)

        # CPF
        cpfInput = self.driver.find_element_by_xpath("//input[@name='cpf']")
        cpfInput.clear()
        cpfInput.send_keys(self.cpf)

        time.sleep(6)
        self.NextStep2()
        time.sleep(6)

        # Full Name

        nameInput = self.driver.find_element_by_xpath(
            "//input[@name='nomeCompleto']")
        nameInput.clear()
        nameInput.send_keys(self.name)

        # Mom

        nameMomInput = self.driver.find_element_by_xpath(
            "//input[@name='nomeMae']")
        nameMomInput.clear()
        nameMomInput.send_keys(self.mae)

        # Birthday

        birthDayInput = self.driver.find_element_by_xpath(
            "//input[@name='nascimento']")
        birthDayInput.clear()
        birthDayInput.send_keys(self.dataNascimento)

        time.sleep(6)
        self.NextStep3()
        time.sleep(6)

        # CEP

        cepInput = self.driver.find_element_by_xpath(
            "//input[@name='cep']")
        cepInput.clear()
        cepInput.send_keys(self.cep)

        time.sleep(3)

        # Number House

        numeroCasaInput = self.driver.find_element_by_xpath(
            "//input[@name='number']")
        numeroCasaInput.clear()
        numeroCasaInput.send_keys(self.numeroCasa)

        time.sleep(4)
        self.NextStep4()
        time.sleep(6)
        self.NextStep4()
        time.sleep(6)

        # SMS

        smsInput = self.driver.find_element_by_xpath(
            "//input[@name='token']")
        smsInput.clear()
        smsInput.send_keys(self.sms)

        time.sleep(1)
        self.NextSubmit()

        self.getFatura()

    def getFatura(self):
        time.sleep(2)
        button = self.driver.find_element_by_class_name('gtmelementevent')
        button.click()

    def migracaoLinha(self):
        time.sleep(2)
        button = self.driver.find_element_by_xpath(
            "//span[@id='tipoLinha-3']")
        button.click()

    def fluxoCadastroMigracao(self):
        self.entrarModal()
        self.migracaoLinha()
        self.preencherDados()

    def fluxoCadastro(self):
        self.entrarModal()
        # self.escolherPlano()
        self.preencherDados()


Bot = TimControleFluxoPos()

Bot.fluxoCadastro()
