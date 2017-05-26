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

order_work = (".//*[@id='app']/div/div[1]/div/div/div/div[3]/div[3]/div/span")
date = (".input.input--fs-14.text--fs-14.react-datepicker-ignore-onclickoutside")
date_click = (".//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div/label/div/input")
work_theme = (".//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div/form/div[1]/div/div[3]/div/label/textarea")
specify_a_task = (".//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div/form/div[2]/div/div/div/div/div[2]")
direction = (".//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div/form/div[3]/div/div[1]/div/label/textarea")
extra_requirement = (".//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div/form/div[3]/div/div[2]/div/label/textarea")
send_request = (".//*[@id='app']/div/div[3]/div/div[2]/div/div[2]/div/form/div[6]/div/div/span/span")
cross = (".//*[@id='app']/div/div[3]/div/div[2]/div/div[1]/div[2]/span/span")





def sendOrder(driver, theme):
	try:
		driver.find_element_by_xpath(order_work).click()
		print(u'Заказать работу -                           ОК')
	except:
		print(u'Заказать работу -                           ОШИБКА')
	time.sleep(2)
	try:
		driver.find_element_by_xpath(date_click).click()
		print(u'Клик -                                      ОК')
	except:
		print(u'Клик -                                      ОШИБКА')
	try:
		send = driver.find_element_by_css_selector(date)
		send.send_keys(u"11.03.2088")
		print(u'Корректная дата напечатана -                ОК')
	except:
		print(u'Корректная дата напечатана -                ОШИБКА')
	try:
		driver.find_element_by_xpath(work_theme).click()
		print(u'Клик -                                      ОК')
	except:
		print(u'Клик -                                      ОШИБКА')
	try:
		send = driver.find_element_by_xpath(work_theme)
		send.send_keys(theme)
		print(u'Тема напечатана -                           ОК')
	except:
		print(u'Тема не напечатана -                        ОШИБКА')
	try:
		driver.find_element_by_xpath(specify_a_task).click()
		print(u'Уточнить задание -                          ОК')
	except:
		print(u'Уточнить задание -                          ОШИБКА')
	try:
		driver.find_element_by_xpath(direction).click()
		print(u'Клик -                                      ОК')
	except:
		print(u'Клик -                                      ОШИБКА')
	try:
		send = driver.find_element_by_xpath(direction)
		send.send_keys(u"Test")
		print(u'Направление напечатано -                    ОК')
	except:
		print(u'Направление не напечатано -                 ОШИБКА')
	try:
		driver.find_element_by_xpath(extra_requirement).click()
		print(u'Клик -                                      ОК')
	except:
		print(u'Клик -                                      ОШИБКА')
	try:
		send = driver.find_element_by_xpath(extra_requirement)
		send.send_keys(u"Test")
		print(u'Доп.требования напечатано -                 ОК')
	except:
		print(u'Доп.требования не напечатано -              ОШИБКА')
	try:
		driver.find_element_by_xpath(send_request).click()
		print(u'Заявка отправлена -                         ОК')
	except:
		print(u'Заявка отправлена -                         ОШИБКА')
	try:
		driver.find_element_by_xpath(cross).click()
		print(u'Модальное окно закрыто -                    ОК')
	except:
		print(u'Модальное окно не закрыто -                 ОШИБКА')


