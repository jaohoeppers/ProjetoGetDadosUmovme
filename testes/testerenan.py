from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
import glob
import time

# Inicia o processo de extração de dados
WebDriverWait(navegador, timeout).until(
    EC.element_to_be_clickable((By.ID, "menu"))
).click()
WebDriverWait(navegador, timeout).until(
    EC.presence_of_element_located((By.ID, "iframemenu"))
)
# Entra no menu de relatórios IFRAME
navegador.switch_to.frame(navegador.find_element(By.ID, "iframemenu"))
element = WebDriverWait(navegador, timeout).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div[2]/div/div[5]/div/div[2]/div/div[7]/a")
    )
)
element.click()
element = WebDriverWait(navegador, timeout).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/div[2]/div/div[5]/div/div[2]/div/div[7]/ul/li[11]/a")
    )
)
element.click()
element = WebDriverWait(navegador, timeout).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div/div[2]/div/div[5]/div/div[2]/div/div[7]/ul/li[11]/ul/li[1]/a",
        )
    )
)
element.click()

# Volta para o frame original
navegador.switch_to.default_content()
# Entra no iframe do relatório
WebDriverWait(navegador, timeout).until(
    EC.presence_of_element_located((By.ID, "iframeSCP089A1-2"))
)
navegador.switch_to.frame(navegador.find_element(By.ID, "iframeSCP089A1-2"))

# Seleciona o filtro de data
dataInicialEncerranento = WebDriverWait(navegador, timeout).until(
    EC.presence_of_element_located((By.ID, "DADATAOS"))
)
dataInicialEncerranento.clear()
dataInicialEncerranento.send_keys("01/01/2021")

dataInicialAbertura = WebDriverWait(navegador, timeout).until(
    EC.presence_of_element_located((By.ID, "DADATA"))
)
dataInicialAbertura.clear()
dataInicialAbertura.send_keys("01/01/2021")

# Aplica o filtro
WebDriverWait(navegador, timeout).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="entrar"]/div/div/div[2]/div[4]/button')
    )
).click()

# Entra no frame dos dados filtrados
# Entra no iframe do relatório
WebDriverWait(navegador, timeout).until(
    EC.presence_of_element_located((By.ID, "frameImp"))
)
navegador.switch_to.frame(navegador.find_element(By.ID, "frameImp"))