# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as beatsop
import re

login_client = (".//*[@id='app']/div/div/div[2]/div/div/div[2]/div[1]/form/div[1]/div[1]/div/label/input")
password_client = (".//*[@id='app']/div/div/div[2]/div/div/div[2]/div[1]/form/div[1]/div[2]/div/label/input")
sign_in_client = (".button.button--teal-a700")
exit = (".//*[@id='app']/div/div[1]/div/div/div/div[3]/div[5]/div/span")

def clientSignIn(driver, login, password):
	try:
		send = driver.find_element_by_xpath(login_client)
		send.send_keys(login)
		print(u'Логин введен -                              ОК')
	except:
		print(u'Логин не введен -                           ОШИБКА')

	try:
		send = driver.find_element_by_xpath(password_client)
		send.send_keys(password)
		print(u'Пароль введен -                             ОК')
	except:
		print(u'Пароль не введен -                          ОШИБКА')

	try:
		driver.find_element_by_css_selector(sign_in_client).click()
		print(u'Вход произведен -                           ОК')
	except:
		print(u'Вход не выполнен -                          ОШИБКА')




def clientSignOut(driver):
	try:
		driver.find_element_by_xpath(exit).click()
		print(u'Выход с клиента произведен -                ОК')
	except:
		print(u'Выход с клиента не произведен -             ОШИБКА')

