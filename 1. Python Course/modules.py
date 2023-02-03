# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
import datetime
from datetime import date
import time
from time import time
from camelcase import CamelCase

today_es = datetime.date.today()
print(today_es)


time_es = time()
print(time_es)

c_es = CamelCase()
print(c_es.hump("fikrimin ince gülü"))



import validator
email_es = "denemeasdaco"

if validator.validate_email(email_es):
    print("Email is valid")
else:
    print("email is bad")