# -*- coding: utf-8 -*-

import string
import random
from cabinets.client_cabinet import *
from cabinets.manager_cabinet import *

def random_generator(size=30, chars=string.ascii_uppercase + string.digits):
	    return 'autotest_' + ''.join(random.choice(chars) for x in range(size))

theme = random_generator()

client = Client()
client.logIn(u"pass", u"pass")
client.sendOrder(theme)
# client.logOut()


manager = Manager()
manager.logIn(u"pass", u"pass")
manager.setCost(theme, 1000, 500, 200)
manager.findLid(theme)
manager.findOffer(theme)
# manager.logOut()