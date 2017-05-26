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
import string
import random


login_manager = (".//*[@id='application']/div/div/div[2]/div/div/div[2]/div[1]/form/div[1]/div[1]/div/label/input")
password_manager = (".//*[@id='application']/div/div/div[2]/div/div/div[2]/div[1]/form/div[1]/div[2]/div/label/input")
sign_in_manager = (".//*[@id='application']/div/div/div[2]/div/div/div[2]/div[1]/form/div[2]/div/span/span/span[1]")
manager_sign_out = (".//*[@id='application']/div/div[1]/div/div/div/div[3]/div[5]/span/span")


def managerSignIn(driver, login, password):

	try:
		send = driver.find_element_by_xpath(login_manager)
		send.send_keys(login)
		print(u'Логин введен -                              ОК')
	except:
		print(u'Логин не введен -                           ОШИБКА')
	try:
		send = driver.find_element_by_xpath(password_manager)
		send.send_keys(password)
		print(u'Пароль введен -                             ОК')
	except:
		print(u'Пароль не введен -                          ОШИБКА')
	try:
		driver.find_element_by_xpath(sign_in_manager).click()
		print(u'Вход произведен -                           ОК')
	except:
		print(u'Вход не выполнен -                          ОШИБКА')



def managerSignOut(driver):
	try:
		driver.find_element_by_xpath(manager_sign_out).click()
		print(u'Выход с клиента произведен -                ОК')
	except:
		print(u'Выход с клиента не произведен -             ОШИБКА')

