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

search_random_words = (".//*[@id='application']/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/label/input")
find_orders = (".//*[@id='application']/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[3]/div[2]/span/span/span[1]")
offer_path = (".block--block.text--grey.text--fs-12>a")

def findOffer(driver, theme):
	try:
		driver.find_element_by_xpath(search_random_words).click()
		send = driver.find_element_by_xpath(search_random_words)
		send.send_keys(Keys.CONTROL + "a");
		send.send_keys(Keys.BACK_SPACE)
		print(u'Тема заказа очищена -                       ОК')
	except:
		print(u'Тема заказа не очищена -                    ОШИБКА')

	try:
		send = driver.find_element_by_xpath(search_random_words)
		send.send_keys(theme)
		print(u'Поиск темы заказа -                         ОК')
	except:
		print(u'Поиск темы заказа -                         ОШИБКА')

	try:
		driver.find_element_by_xpath(find_orders).click()
		print(u'Найти заказы -                              ОК')
	except:
		print(u'Найти заказы -                              ОШИБКА')

	try:
		value = driver.find_element_by_css_selector(offer_path)
		result = value.get_attribute('text')
		if result == u'Предложение':
			driver.find_element_by_css_selector(offer_path).click()
			print(u'Произведен клик по Предложение -            ОК')
			driver.switch_to.window(driver.window_handles[-1])
			print(u'Переход на новое окно -                     ОК')
			driver.close()
			print(u'Закрытие нового окна -                      ОК')
			driver.switch_to.window(driver.window_handles[0])
		else:
			print(u'Текст ссылки не равен Предложение -         ОШИБКА')
			raise SystemExit(0)
	except:
		print(u'Не удалось найти пусть к ссылке Лид -       ОШИБКА')
		


