from monitorme.settings import *

import django_heroku 

	
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

django_heroku.settings(locals())