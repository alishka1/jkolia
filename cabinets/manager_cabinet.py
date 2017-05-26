# -*- coding: utf-8 -*-

from cabinet import *
from manager.auth import *
from manager.set_cost import *
from manager.lid import *
from manager.offer import *

class Manager(Cabinet):
	def __init__(self):
		Cabinet.__init__(self, u"http://pass")


	def logIn(self, login, password):
		managerSignIn(self._driver, login, password)
		time.sleep(3)

	def logOut(self):
		managerSignOut(self._driver)
		time.sleep(3)

	def setCost(self, theme, one_thousand, five_hundred, two_hundred):
		setCost(self._driver, theme, one_thousand, five_hundred, two_hundred)
		time.sleep(3)

	def findLid(self, theme):
		findLid(self._driver, theme)
		time.sleep(3)

	def findOffer(self, theme):
		findOffer(self._driver, theme)
		time.sleep(3)
		
