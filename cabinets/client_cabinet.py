# -*- coding: utf-8 -*-

from cabinet import *
from client.auth import *
from client.send_order import *


class Client(Cabinet):
	def __init__(self):
		Cabinet.__init__(self, u"http://pass")


	def logIn(self, login, password):
		clientSignIn(self._driver, login, password)
		time.sleep(3)

	def logOut(self):
		clientSignOut(self._driver)
		time.sleep(3)

	def sendOrder(self, theme):
		sendOrder(self._driver, theme)
		time.sleep(3)



