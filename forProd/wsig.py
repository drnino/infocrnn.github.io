# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys
path = '/home/ninodominguezmd/mysite/'
if path not in sys.path:
    sys.path.append(path)
   #sys.path.insert(0, path)

# import flask app but need to call it "application" for WSGI to work
from flask_app import app as application  # noqa
