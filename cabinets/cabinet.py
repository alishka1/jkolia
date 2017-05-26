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


class Cabinet:
	def __init__(self, url):
		self._driver = webdriver.Chrome("chromedriver")
		self._driver.set_page_load_timeout(30)
		self._driver.get(url)
		self._driver.implicitly_wait(10)
		self._driver.maximize_window()
		time.sleep(3)