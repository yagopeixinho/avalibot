import time
from selenium import webdriver
from selenium.webdriver.common.by import By

optionsQuality = ['00', '02', '04,', '06', '08', '10']
optionSelected = input(
    "Escolha a opção avaliativa: (1. Um - Fraco) (2. Dois) (3. Três) (4. Quatro) (5. Cinco - Excelente) (6. Não sei responder / não utilizei o serviço): ")
quality: any

if optionSelected == "1":
    print("Opção selecionada com sucesso.")
    quality = optionsQuality[0]
elif optionSelected == "2":
    print("Opção selecionada com sucesso.")
    quality = optionsQuality[1]
elif optionSelected == "3":
    print("Opção selecionada com sucesso.")
    quality = optionsQuality[2]
elif optionSelected == "4":
    print("Opção selecionada com sucesso.")
    quality = optionsQuality[3]
elif optionSelected == "5":
    print("Opção selecionada com sucesso.")
    quality = optionsQuality[4]
elif optionSelected == "6":
    print("Opção selecionada com sucesso.")
    quality = optionsQuality[5]
else:
    print("Opção inválida!")


class Avalibot():
    def __init__(self, quality):
        self.template = "//input[@id = 'VanillaTheme_wt6_block_wtMainContent_wtQuestaoList_ctl{_id}_wt4_wtListRecords1_ctl{quality}_wtradio']"
        self.quality = quality
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(
            "https://aluno.uninassau.edu.br/aluno/IDP_ROUTE_LOGIN_ALUNO3.aspx?Hash=CCQVENXTRHZNEVUFFH5XJABCNSLJAWON&HashClaim=A5QHUBVTOR5WCWVTKLCPFDYAUZ99BSBA")

    def start(self):
        _id = 0
        i = 0

        while i < 60:
            radioElement = self.driver.find_element(
                By.XPATH, self.template.format(_id="%02d" % (_id,), quality=self.quality))

            radioElement.click()
            _id = _id + 2
            i = i + 1
            time.sleep(1)


avalibot = Avalibot(quality)
