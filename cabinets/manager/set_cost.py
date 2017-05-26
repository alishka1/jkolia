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
random_theme_in_manager = (".//*[@id='application']/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/span/span/span/span[3]/span[1]")
open_brief = (".//*[@id='application']/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div/div[1]/div/div/div[2]/span/span")
cost = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[6]/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]")
cost_of_work = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[6]/div/div/div/div/div[1]/div/label/input")
cost_tick = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[6]/div/div/div/div/div[1]/div/div/div/span[1]/span")
estimated_cost = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[6]/div/div/div/div/div[2]/div[1]")
set_estimated_cost = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[6]/div/div/div/div/div[2]/div/label/input")
estimated_cost_tick = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[6]/div/div/div/div/div[2]/div/div/div/span[1]/span")
royalties = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[6]/div/div/div/div/div[3]/div[1]")
set_royalties_cost = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[6]/div/div/div/div/div[3]/div/label/input")
royalties_tick = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[6]/div/div/div/div/div[3]/div/div/div/span[1]/span")
arrow_brief = (".//*[@id='application']/div/div[2]/div[2]/div[3]/div[1]/div[1]/span/span")
arrow_info_about_order = (".//*[@id='application']/div/div[2]/div[2]/div[2]/div[1]/div[1]/span/span")





def setCost(driver, theme, one_thousand, five_hundred, two_hundred):
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
		driver.find_element_by_xpath(random_theme_in_manager).click()
		print(u'Вход в заказ -                              ОК')
	except:
		print(u'Вход в заказ -                              ОШИБКА')

	time.sleep(1)
	try:
		driver.find_element_by_xpath(open_brief).click()
		print(u'Открыть бриф -                              ОК')
	except:
		print(u'Открыть бриф -                              ОШИБКА')

	try:
		element = driver.find_element_by_xpath(cost)
		actions = ActionChains(driver)
		actions.double_click(element).perform()
		print(u'Стоимость клик -                            ОК')
	except:
		print(u'Стоимость клик -                            ОШИБКА')

	try:
		send = driver.find_element_by_xpath(cost_of_work)
		send.send_keys(one_thousand)
		print(u'Стоимость установлена -                     ОК')
	except:
		print(u'Стоимость не установлена -                  ОШИБКА')

	time.sleep(2)
	try:
		driver.find_element_by_xpath(cost_tick).click()
		print(u'Галочка нажата -                            ОК')
	except:
		print(u'Галочка не нажата -                         ОШИБКА')

	try:
		element = driver.find_element_by_xpath(estimated_cost)
		actions = ActionChains(driver)
		actions.double_click(element).perform()
		print(u'Расчетная стоимость клик -                  ОК')
	except:
		print(u'Расчетная стоимость клик -                  ОШИБКА')

	try:
		send = driver.find_element_by_xpath(set_estimated_cost)
		send.send_keys(five_hundred)
		print(u'Расчетная стоимость установлена -           ОК')
	except:
		print(u'Расчетная стоимость не установлена -        ОШИБКА')

	time.sleep(2)
	try:
		driver.find_element_by_xpath(estimated_cost_tick).click()
		print(u'Галочка нажата -                            ОК')
	except:
		print(u'Галочка не нажата -                         ОШИБКА')

	try:
		element = driver.find_element_by_xpath(royalties)
		actions = ActionChains(driver)
		actions.double_click(element).perform()
		print(u'Гонорар автора клик -                       ОК')
	except:
		print(u'Гонорар автора клик -                       ОШИБКА')

	try:
		send = driver.find_element_by_xpath(set_royalties_cost)
		send.send_keys(two_hundred)
		print(u'Гонорар автора установлен -                 ОК')
	except:
		print(u'Гонорар автора не установлен -              ОШИБКА')

	time.sleep(2)
	try:
		driver.find_element_by_xpath(royalties_tick).click()
		print(u'Галочка нажата -                            ОК')
	except:
		print(u'Галочка не нажата -                         ОШИБКА')

	try:
		driver.find_element_by_xpath(arrow_brief).click()
		print(u'Галочка нажата -                            ОК')
	except:
		print(u'Галочка не нажата -                         ОШИБКА')
	time.sleep(1)
	try:
		driver.find_element_by_xpath(arrow_info_about_order).click()
		print(u'Галочка нажата -                            ОК')
	except:
		print(u'Галочка не нажата -                         ОШИБКА')

